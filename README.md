 File Integrity Monitor (FIM) com Interface Gráfica

Um sistema defensivo desenvolvido em Python para monitorar a integridade de arquivos críticos em tempo real. A ferramenta utiliza hashes criptográficos para criar impressões digitais dos dados e dispara alertas visuais imediatos na interface caso ocorra qualquer modificação não autorizada (tentativa de breach).

---

 Funcionalidades
* Detecção por SHA-256: Utiliza o algoritmo padrão da criptografia de segurança para garantir que nenhuma alteração passe despercebida.
* Interface Gráfica (GUI): Visual customizado em Modo Escuro (estilo Matrix) utilizando a biblioteca nativa `tkinter`.
* Processamento em Segundo Plano (Multi-threading): O loop de verificação roda em uma `Thread` separada usando a biblioteca `threading`. Isso garante que a interface gráfica nunca congele ou trave enquanto o monitor está ativo.
* Modo de Investigação Forense: Inclui um botão de interrupção tática que congela o scanner com segurança, permitindo que a equipe de resposta a incidentes analise a anomalia sem novos alertas na tela e resete o painel para o estado padrão quando terminar.

---

 Libs. Utilizadas
* Python 3 (Linguagem principal)
* Hashlib (Geração de Hashes criptográficos SHA-256)
* Threading (Execução em segundo plano)
* Tkinter (Construção da interface de usuário)

---

 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Baixe o arquivo do código deste repositório.
3. Abra o script e altere a variável `caminho` com o diretório exato do arquivo que você deseja proteger.
4. Execute o programa pelo seu terminal ou editor de código:
   ```bash
   python monitor_visual.py
   ```
5. Clique em Iniciar Monitoramento e faça um teste alterando uma única letra do seu arquivo de texto para ver o sistema disparar os alertas em tempo real no terminal e mudar o status da tela para vermelho!
