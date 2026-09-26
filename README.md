# Foltz WBS 🔔

![Python](https://img.shields.io/badge/Python-3-blue) ![Requests](https://img.shields.io/badge/requests-2.32-green) ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Termux-orange) ![License](https://img.shields.io/badge/license-MIT-yellow)

**Foltz WBS** é uma ferramenta interativa em Python para gerenciar e usar webhooks de forma eficiente: adicionar, listar, verificar e deletar webhooks, além de enviar mensagens em massa para os webhooks configurados.

**Idioma:** Português (este arquivo) • [English](README.en.md) • [Español](README.es.md)

## Sumário

- [Recursos](#recursos)
- [Pré-requisitos](#pré-requisitos)
- [Estrutura](#estrutura)
- [Começando](#começando)
- [Como usar](#como-usar)
- [Personalização](#personalização)
- [Licença](#licença)
- [Contato](#contato)

## Recursos

- Adicionar novos webhooks
- Deletar webhooks existentes
- Listar todos os webhooks salvos
- Verificar se os webhooks estão funcionando
- Enviar mensagens em massa para os webhooks
- Banners ASCII personalizáveis
- Efeito de máquina de escrever no terminal

## Pré-requisitos

- **Python 3.x** instalado
- **pip** para instalar as dependências (`colored`, `requests`)

## Estrutura

```
FoltzWBS/
├── LICENSE
├── README.md
└── foltz-wbs/
    ├── main.py                  # script principal (menu interativo)
    ├── requirements.txt         # dependências (colored, requests)
    ├── install_requirements.bat # instala as dependências (Windows)
    ├── start.bat                # inicia o programa (Windows)
    ├── webhooks.txt             # webhooks salvos
    └── ascii_banners/           # banners personalizáveis
```

## Começando

Siga estas etapas para instalar e usar o Foltz WBS no seu sistema.

### 📥 Instalação

#### Windows

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Instale as dependências:**

   Execute o arquivo `install_requirements.bat`:

   ```bash
   install_requirements.bat
   ```

3. **Inicie o script:**

   Execute o arquivo `start.bat`:

   ```bash
   start.bat
   ```

#### Linux

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o script:**

   ```bash
   python main.py
   ```

#### Termux

1. **Instale Python e Git:**

   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. **Clone o repositório e instale as dependências:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   pip install -r requirements.txt
   ```

3. **Execute o script:**

   ```bash
   python main.py
   ```

## Como Usar

1. **Inicie o Foltz WBS.**
2. **Escolha uma opção do menu:**
   - **Adicionar Webhook**: Adicione uma nova URL de webhook (salva em `webhooks.txt`).
   - **Deletar Webhook**: Remova um webhook existente.
   - **Listar Webhooks**: Veja todos os webhooks salvos.
   - **Verificar Webhooks**: Cheque se os webhooks estão funcionando.
   - **Enviar Mensagens**: Envie mensagens em massa para os webhooks.

## Arquivos `.bat`

- **`install_requirements.bat`**: Instala as bibliotecas necessárias (`colored`, `requests`).
- **`start.bat`**: Inicia o script principal.

## Personalização

- **Banners**: Personalize os banners editando os arquivos em `ascii_banners/`.
- **Efeito de Texto**: Ajuste o efeito de máquina de escrever no script conforme preferir.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:

- **Foltz** - [GitHub](https://github.com/foltzbr)
