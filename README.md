# Case_Techway

## Task:

- Título: Site não abre corretamente [Bug]
- Status: Resolvido
- Nome do cliente: JJ Investimentos LTDA.
- CNPJ do cliente: 45.244.282/0001-63
- Solicitante: Marcelo Costa (marcelo.costa@softway.com.br)
- Chave: OSD-2368

- Estimativa: 8hs
- Horas trabalhadas: 8hs
- Data da Abertura: 27/11/2023
- Prazo limite:  08/12/2023
- Responsável: Lucas Matos da Silva

## Notas sobre Problemas e Soluções

### Arquivos Estáticos
- **Problema:** Os arquivos estáticos não estavam carregando corretamente, o que afetava os estilos e imagens.
- **Solução Aplicada:** Ajustamos as configurações no arquivo `jj_investimento/settings.py` para o Django utilizar os recursos estáticos. Adicionamos um caminho `STATICFILES_DIRS` para incluir a pasta `page_app/static` como um diretório de arquivos estáticos.

### Nomes Incorretos de Imagens
- **Problema:** Alguns nomes de imagens estavam errados.
- **Solução Aplicada:** Renomeamos as imagens corretamente na pasta `page_app/static/page_app/img/`.

### Links do Rodapé
- **Problema:** Os links do rodapé estavam apontando para lugares que não existiam.
- **Solução Aplicada:** Corrigimos os links do rodapé no arquivo `page_app/templates/page_app/partial/footer.html`.

### Caminho da Imagem do Logotipo
- **Problema:** O caminho da imagem do logotipo no cabeçalho estava errado.
- **Solução Aplicada:** Arrumamos o caminho da imagem do logotipo no arquivo `page_app/templates/page_app/partial/header.html` para usar os arquivos estáticos corretamente.

### Caminho das Imagens na Página Inicial
- **Problema:** Os caminhos das imagens na página inicial não estavam considerando os arquivos estáticos.
- **Solução Aplicada:** Arrumamos os caminhos e o tratamento para os arquivos estáticos das imagens na página inicial, no arquivo `page_app/templates/page_app/partial/home.html`.

### Rota para "Nossos Serviços"
- **Problema:** Não tinha uma rota definida para a página "Nossos Serviços".
- **Solução Aplicada:** Adicionamos um caminho para mostrar a página "Nossos Serviços" no arquivo `page_app/urls.py`.

### Atualização das Informações de Contato
- **Problema:** As informações de contato na página "contato.html" estavam antigas, com endereço de e-mail, número de telefone e link do WhatsApp errados.
- **Solução Aplicada:** Atualizamos as informações de contato, corrigindo o endereço de e-mail para "contato@jjinvestimento.com.br", ajustando o link do WhatsApp para o número +1 (25) 2680-4187 e atualizando o número de telefone para +55 (41) 3223-2112.
