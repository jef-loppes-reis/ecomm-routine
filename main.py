"""--- Rotina de E-commerce ---"""

import os
from typing import List, Dict, Any
from datetime import datetime
import time

from rich import print

from constants import PROJECTS


class Scheduler:

    def __init__(self):
        self.path_root = os.path.dirname(os.path.abspath(__file__))
        self.path_data = os.path.join(self.path_root, "data")
        self.path_postgres_updated = os.path.join(self.path_data, "postgres_updated.txt")

    def verify_update_postgres(self) -> tuple[bool, int]:
        with open(self.path_postgres_updated, "r") as f:
            update_postgres: str = f.read()

        if datetime.now().hour == int(update_postgres):
            with open(self.path_postgres_updated, "w") as f:
                f.write(str(-1))
            return True, int(update_postgres)
        return False, int(update_postgres)

    def verify_dia_semana(self) -> str:
        dia_semana = datetime.now().weekday()
        match dia_semana:
            case 0:
                return "Segunda-feira"
            case 1:
                return "Terça-feira"
            case 2:
                return "Quarta-feira"
            case 3:
                return "Quinta-feira"
            case 4:
                return "Sexta-feira"
            case 5:
                return "Sábado"
            case 6:
                return "Domingo"
            case _:
                return "Dia da semana não encontrado"

class EcommRoutine:

    def __init__(self):
        self.path_root = os.path.dirname(os.path.abspath(__file__))
        self.path_data = os.path.join(self.path_root, "data")
        self.scheduler = Scheduler()

    def _run_project_system(self, path: str, name_module: str):
        os.system(f"cd {path}")
        os.system(f"uv run {name_module}")
        os.system(f"cd {self.path_root}")

    def run_projects(self, list_projects: Dict[str, List[Dict[str, Any]]]):
        for project_name, project_data in list_projects.items():
            for project in project_data:
                try:
                    # Verifica se o dia da semana é valido
                    if project.get('days'):
                        if self.scheduler.verify_dia_semana() in project.get('days', []):
                            # Verifica se o horario especifico é valido
                            if project.get('hour_specific'):
                                if datetime.now().hour in project.get('hour_specific', []):
                                    self._run_project_system(
                                        path=project.get('path', ''),
                                        name_module=project.get('name_module', ''))
                                    print(f"Project {project_name} executed successfully!")
                                    print('=-'*100)
                                    continue
                            # Verifica se o horario comercial é valido
                            if project.get('hour'):
                                if datetime.now().hour in project.get('hour', []):
                                    self._run_project_system(
                                        path=project.get('path', ''),
                                        name_module=project.get('name_module', ''))
                                    print(f"Project {project_name} executed successfully!")
                                    print('=-'*100)
                                    continue
                except Exception as e:
                    print(f"Error: {e}")
                    print('=-'*100)
                    continue

    def main(self):
        while True:
            postgres_updated, postgres_hour = self.scheduler.verify_update_postgres()
            if postgres_updated:
                self.run_projects(list_projects=PROJECTS)
            time.sleep(60 * 2)


if __name__ == "__main__":
    ecomm_routine = EcommRoutine()
    ecomm_routine.main()
