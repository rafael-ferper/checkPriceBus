# Bus Price Checker

## Descrição
Este é um bot Python que verifica o preço das passagens de ônibus de Itajubá para Campinas no site ClickBus a cada hora. Se o preço cair abaixo de um determinado valor, o bot enviará um e-mail para notificar o usuário.

## Como funciona
O bot usa a biblioteca `requests` para fazer uma solicitação HTTP para a página da web. Em seguida, usa `BeautifulSoup` para analisar o conteúdo HTML da página e extrair o preço da passagem. Se o preço for menor que o valor definido, o bot usa `smtplib` para enviar um e-mail ao usuário.

## Como usar
1. Clone este repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure as variáveis de ambiente `USER` e `PASSWORD` com suas informações de login do Gmail.
4. Execute o script com `python lambda_function.py`.

## AWS Lambda
Este bot foi projetado para ser executado na AWS Lambda. Para implantar o bot na AWS Lambda, siga estas etapas:
1. Crie uma nova função Lambda no console AWS.
2. Carregue o código para a função Lambda.
3. Configure as variáveis de ambiente `USER` e `PASSWORD` na função Lambda.
4. Configure o AWS EventBridge para acionar a função Lambda a cada hora.

## Aviso
Este bot foi criado para fins educacionais e não deve ser usado para atividades que violem os Termos de Serviço do site alvo. Além disso, o envio de e-mails através do Gmail usando smtplib pode exigir que você permita aplicativos menos seguros na sua conta do Google. Use com cautela.
