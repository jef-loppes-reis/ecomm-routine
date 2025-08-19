# Ecomm Routine

Sistema automatizado de rotinas para e-commerce que executa projetos em horários específicos baseado em configurações predefinidas.

## 📋 Descrição

O **Ecomm Routine** é um scheduler inteligente que gerencia a execução de múltiplos projetos de e-commerce de forma automatizada. O sistema monitora continuamente o horário atual e executa diferentes rotinas baseado em:

- Dia da semana
- Horário específico
- Horário comercial
- Estado de atualização do PostgreSQL

## 🚀 Funcionalidades

- **Agendamento Inteligente**: Executa projetos baseado em configurações de horário e dia da semana
- **Monitoramento Contínuo**: Verifica condições a cada 2 minutos
- **Controle de Estado**: Gerencia atualizações do PostgreSQL para evitar execuções duplicadas
- **Tratamento de Erros**: Continua funcionando mesmo se um projeto falhar
- **Logs Coloridos**: Interface visual rica para acompanhamento das execuções

## 🛠️ Tecnologias

- **Python 3.13+**
- **UV** (gerenciador de pacotes)
- **Rich** (interface de terminal)
- **Loguru** (sistema de logs)
- Bibliotecas customizadas para integração com APIs de e-commerce

## 📦 Instalação

### Pré-requisitos

- Python 3.13 ou superior
- UV (gerenciador de pacotes)
- Git

### Passos de Instalação

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd ecomm-routine
   ```

2. **Instale as dependências:**

   ```bash
   uv sync
   ```

3. **Configure os projetos** (veja seção de Configuração)

## ⚙️ Configuração

### Estrutura de Projetos

Os projetos são configurados no arquivo `constants.py` através do dicionário `PROJECTS`. Cada projeto deve seguir a estrutura:

```python
"nome_do_projeto": [
    {
        "name_module": "main.py",           # Arquivo principal para execução
        "path": "../caminho/do/projeto",    # Caminho relativo do projeto
        "hour": [7, 8, 9, 10],             # Horários de execução (opcional)
        "days": ["Segunda-feira", "Terça-feira"], # Dias da semana (opcional)
        "hour_specific": [10, 14, 16],     # Horários específicos (opcional)
    }
]
```

### Parâmetros de Configuração

| Parâmetro | Tipo | Descrição | Obrigatório |
|-----------|------|-----------|-------------|
| `name_module` | str | Nome do arquivo Python principal | ✅ |
| `path` | str | Caminho relativo do projeto | ✅ |
| `hour` | List[int] | Lista de horários para execução | ❌ |
| `days` | List[str] | Lista de dias da semana | ❌ |
| `hour_specific` | List[int] | Horários específicos prioritários | ❌ |

### Constantes Disponíveis

```python
# Horários comerciais
HORARIO_INICIAL_COMERCIAL = 7     # 7h
ULTIMO_HORARIO_COMERCIAL = 19     # 19h
ULTIMO_HORARIO_SABADO = 16        # 16h

# Listas de horários
HORARIO_COMERCIAL = [7, 8, 9, ..., 18]
HORARIO_COMERCIAL_SABADO = [7, 8, 9, ..., 15]
```

## 🎯 Como Usar

### Execução Principal

```bash
# Executar o sistema de rotinas
uv run main.py
```

### Execução de Teste

```bash
# Para testes e desenvolvimento
uv run teste.py
```

## 📋 Lógica de Execução

O sistema segue a seguinte prioridade de execução:

1. **Verificação do dia da semana**: O projeto só executa nos dias especificados
2. **Horários específicos**: Se definido, tem prioridade sobre horário comercial
3. **Horário comercial**: Executa nos horários definidos na lista `hour`
4. **Estado do PostgreSQL**: Controla execuções para evitar duplicatas

### Fluxo de Funcionamento

```text
O sistema executa em um loop contínuo que:

1. Verifica se o PostgreSQL foi atualizado na hora atual
2. Se sim, itera sobre todos os projetos configurados
3. Para cada projeto, verifica:
   - Se hoje é um dia válido para execução
   - Se a hora atual permite execução (específica ou comercial)
4. Executa o projeto se todas as condições forem atendidas
5. Aguarda 2 minutos antes da próxima verificação
```

## 📁 Estrutura do Projeto

```text
ecomm-routine/
├── main.py              # Script principal
├── constants.py         # Configurações e constantes
├── teste.py             # Arquivo de testes
├── pyproject.toml       # Configuração do projeto
├── data/
│   └── postgres_updated.txt  # Estado de atualização do PostgreSQL
├── README.md            # Este arquivo
└── uv.lock             # Lock file das dependências
```

## 🔧 Exemplos de Configuração

### Projeto que executa apenas em dias úteis

```python
"update_price_ml": [
    {
        "name_module": "main.py",
        "path": "../update_price_ml",
        "hour": [10, 14, 16],
        "days": ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                 "Quinta-feira", "Sexta-feira"],
        "hour_specific": [],
    }
]
```

### Projeto que executa todos os dias em horário específico

```python
"backup_database": [
    {
        "name_module": "backup.py",
        "path": "../database_backup",
        "hour": [],
        "days": ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                 "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"],
        "hour_specific": [23],  # 23h todos os dias
    }
]
```

### Projeto com múltiplas configurações

```python
"sync_inventory": [
    {
        "name_module": "sync_morning.py",
        "path": "../inventory_sync",
        "hour": [],
        "days": ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                 "Quinta-feira", "Sexta-feira"],
        "hour_specific": [8],  # 8h em dias úteis
    },
    {
        "name_module": "sync_evening.py", 
        "path": "../inventory_sync",
        "hour": [],
        "days": ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                 "Quinta-feira", "Sexta-feira"],
        "hour_specific": [18],  # 18h em dias úteis
    }
]
```

## 🔄 Projetos Configurados Atualmente

O sistema está configurado para executar os seguintes projetos:

### 1. Update Price Storage ML

- **Módulo**: `main.py`
- **Dias**: Segunda a Sexta-feira
- **Horários**: 10h às 15h (horários específicos)
- **Horário comercial**: A partir das 10h

### 2. Update Price Stock Shopee

- **Módulo**: `main.py`
- **Dias**: Segunda a Sexta-feira
- **Horários**: 10h às 15h (horários específicos)
- **Horário comercial**: A partir das 10h

### 3. Database E-comm

- **Módulo**: `main.py --truncate`
- **Dias**: Todos os dias
- **Horários**: 0h às 6h (horários específicos)

### 4. Update CFOP

- **Módulo**: `update.py`
- **Dias**: Todos os dias
- **Horários**: Horário comercial completo (7h às 18h)

## 🐛 Troubleshooting

### Problemas Comuns

1. **Projeto não executa:**
   - Verifique se o caminho está correto
   - Confirme se os dias/horários estão configurados corretamente
   - Verifique se o arquivo `name_module` existe no projeto

2. **Erro de dependências:**

   ```bash
   uv sync --force-reinstall
   ```

3. **Erro de caminho:**
   - Use caminhos relativos a partir da pasta `ecomm-routine`
   - Verifique se o projeto de destino possui `pyproject.toml`

4. **Sistema não reconhece horário:**
   - Verifique o arquivo `data/postgres_updated.txt`
   - O valor `-1` indica que não há restrição de horário
   - Qualquer hora específica impede execução até a próxima hora

## 📝 Logs e Monitoramento

O sistema utiliza **Rich** para exibir logs coloridos:

- ✅ **Verde**: Execução bem-sucedida
- ❌ **Vermelho**: Erro na execução
- ℹ️ **Azul**: Informações gerais

### Exemplo de Saída

```text
Project update_price_storage_ml executed successfully!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Project update_price_stock_shopee executed successfully!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

## 🔧 Desenvolvimento

### Adicionando Novos Projetos

1. **Edite o arquivo `constants.py`**
2. **Adicione uma nova entrada no dicionário `PROJECTS`**
3. **Configure os parâmetros conforme necessário**

Exemplo:

```python
"novo_projeto": [
    {
        "name_module": "main.py",
        "path": "../caminho/do/novo/projeto",
        "hour": HORARIO_COMERCIAL,
        "days": ["Segunda-feira", "Terça-feira"],
        "hour_specific": [14],
    }
]
```

### Testando Configurações

Use o arquivo `teste.py` para testar configurações específicas sem afetar o sistema principal.

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
