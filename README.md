# 🚀 ISP CRM Manager

> Um sistema de gestão de relacionamento com o cliente (CRM) focado em Provedores de Internet (ISPs), desenvolvido com Python e Django.

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 💡 Sobre o Projeto

Este projeto nasceu de uma necessidade prática e da minha experiência profissional atuando no **Suporte Técnico** de provedores de internet. Inspirado na lógica de grandes ERPs do mercado (como o **IXC Soft**), desenvolvi esta solução para simular a centralização de informações vitais da operação.

O objetivo foi criar uma "espinha dorsal" administrativa que permitisse:
1.  **Agilidade no Atendimento:** Localizar o cliente rapidamente (por Nome ou CPF) enquanto ele está na linha.
2.  **Visão Gerencial:** Entender a saúde financeira e técnica do provedor através de dashboards visuais.
3.  **Organização:** Vincular contratos, planos de velocidade e chamados técnicos em um único histórico.

Este projeto demonstra a aplicação prática de conceitos de **Modelagem de Dados (ORM)**, **Autenticação**, **Visualização de Dados** e **Design Responsivo**.

---

## 🛠 Funcionalidades

- **📊 Dashboard Interativa:**
  - KPIs em tempo real: Total de Clientes, Contratos Ativos, Chamados Pendentes e Receita Mensal Estimada.
  - Gráfico dinâmico (Chart.js) para análise visual dos tipos de chamados.
  
- **🔍 Busca Inteligente (Quick Search):**
  - Barra de pesquisa global utilizando `Q Objects` do Django.
  - Localiza clientes instantaneamente por **Nome** ou **CPF/CNPJ**.
  
- **👥 Gestão de Assinantes:**
  - Cadastro completo de clientes com validação.
  - Gestão de Contratos (Status: Ativo, Suspenso, Cancelado).
  - Controle de Planos de Acesso (Velocidade e Valor).
  
- **🔧 Service Desk (Chamados):**
  - Abertura de tickets de suporte (Lentidão, Financeiro, Sem Conexão).
  - Fluxo de status (Aberto -> Em Andamento -> Concluído).

- **🔒 Segurança:**
  - Sistema de login obrigatório para acesso ao painel.
  - Proteção nativa contra ataques comuns (CSRF, SQL Injection).

---

## 💻 Tecnologias Utilizadas

- **Backend:** Python, Django Framework.
- **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsivo).
- **JavaScript:** Chart.js (Integração de gráficos).
- **Banco de Dados:** SQLite (Padrão de desenvolvimento, fácil migração para PostgreSQL).
- **Versionamento:** Git & GitHub.

---

## 🚀 Como rodar o projeto

Siga os passos abaixo para configurar o ambiente de desenvolvimento na sua máquina.

### Pré-requisitos
- Python 3.x instalado.
- Git instalado.

### 1. Clone o repositório
```bash
git clone [https://github.com/huankzera/ispcrm-manager.git](https://github.com/huankzera/ispcrm-manager.git)
cd ispcrm-manager
```
Crie um Ambiente Virtual (Recomendado)
```bash
# No Windows:
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências
```bash
pip install django
# Ou se houver um requirements.txt:
# pip install -r requirements.txt
```
Prepare o Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
```
Crie um Superusuário (Admin)
```bash
python manage.py createsuperuser
```
Inicie o Servidor
```bash
python manage.py runserver

```
Acesse no seu navegador: http://127.0.0.1:8000/


Primeiros Passos no Sistema
Como o banco de dados é novo, a Dashboard aparecerá vazia ("zeros"). Para ver a mágica acontecer:

1- Faça login com o usuário que você criou.

2- Clique em "Painel Admin" no topo ou acesse /admin.

3- Cadastre dados fictícios na seguinte ordem:

4- Crie um Plano de Internet (ex: Fibra 500MB - R$ 99,90).

5- Cadastre um Cliente.

6- Crie um Contrato vinculando esse Cliente ao Plano.

7- Abra um Chamado Técnico para teste.

Volte para a página inicial e veja os gráficos atualizados! 🚀

👨‍💻Autor👨‍💻

Desenvolvido por Matheus Huank. (Projeto criado para fins de estudo e portfólio, aplicando conhecimentos de desenvolvimento Full Stack)



