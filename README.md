# Morse-message
Recebendo mensagens, e as traduzindo de/para morse

## Por que Rabbitmq?
A ideia é uma solução escalável que recebe um código morse e traduz para texto, ou recebe um texto e traduz para código morse. Rabbitmq foi escolhido como framework por ser um dos framework que melhor serve nesse caso, sendo um dos brokers de mensagem mais bem avaliados entre os especialistas. Entre os principais pontos positivos, podem ser destacados a implantação distribuída (distributed deployment), administração e monitoramento, tolerância a falhas, eficiência e facilidade de integração. O rabbitmq é um dos corretores de mensagens (message broker) mais populares da atualidade, justamente por permitir ao desenvolvedor a criar e implementar algo que sirva muito bem a diversas situações. O rabbitmq utiliza o protocolo de mensagens AMQP, que utiliza exchanges como intermediárias para transmitir as mensagens para uma fila, possibilitando o utilização de diversos recursos que podem ser bastante úteis.

## Por que direct?
O rabbitmq utiliza o protocolo de mensagens AMQP, que utiliza exchanges como intermediárias para transmitir as mensagens. Existem quatro tipos de exchange e a que foi implementada nesse código foi a do tipo direct. Esse tipo foi escolhido por vários motivos. O primeiro deles é a necessidade de uma chave, algo parecido com uma senha, para acessar a mensagem. Caso o receptor queira receber determinada mensagem, ele vai precisar saber por qual chave essa mensagem foi enviada. Outra vantagem que o direct permite, é receber apenas algumas mensagens, permitir que os usuários utilizem de determinado código (decidido entre os próprios usuários), para decidir diversos assuntos, como por exemplo, qual a importância, ou a urgência, de determinado assunto, além de permitir que essa mensagem seja acessada por diversas fontes diferentes. Dessa forma, isso permitiria que apenas quem soubesse da chave conseguisse acessar determinada mensagem, e consequentemente traduzi-la. Aliado ao AMQP, isso também diminuiria as chances de perder a mensagem.
  
## Sobre a entrada
Para o código funcionar corretamente, basta que o usuário (com python e rabbitmq instalado) rode primeiramente o código receive_translate.py, com a(s) respectiva(s) chave(s), por exemplo, "py receive_translate.py random_key1 random_key2 e, em seguida, enviar as mensagens através do send_message.py, seguido pela chave pela qual a mensagem deve ser enviada e a mensagem que deve ser enviada, entre aspas (por exemplo, py send_message.py random_key1 "mensagem exemplo"). 
  
#### Quantas vezes executar?
 - Quanto ao receptor das mensagens (receive_translate.py), basta rodar o código uma única vez com a(s) chave(s) para que recebe todas as respectivas mensagens enviadas para aquela(s) chaves. Cada mensagens será impressa em uma única linha, juntamente com sua tradução.
 - Já quanto ao remetente (send_message.py), o usuário não precisará de mante-lo aberto, sendo executado para cada mensagem que desejar enviar.
  
##### Importante!
Caso a mensagem seja enviada sem aspas, o código ainda funcionará, e a mensagem será traduzida. Porém, no caso da tradução de morse para texto, poderá haver um pequeno erro de tradução em que a mensagem será traduzida como uma única palavra, sem espaços. Isso acontece devido ao fato de que, caso a entrada possua mais de um espaço seguido, esses espaços acabam sendo simplicados pelo sistema como se apenas um espaço fosse recebido, resultando em uma tradução para texto sem espaço, como se a mensagem enviada sem espaços duplos. Caso o usuário envie uma palavra para tradução com espaçamento maior que dois, a mensagem traduzida também possuirá esses espaçamentos.
  
 
 ## Quanto à tradução
 A tradução da mensagem é realizada em algumas etapas básicas:
1. Quando o emissor enviar a mensagem, o receptor irá enviar essa mensagem para um tradutor.
2. Identificação do tipo da mensagem recebida: será contabilizada a quantidade de pontos ("."), hífens ("-") e espaços (" "), que são os únicos caracteres presentes em um código morse. Essas quantidades serão somadas, e, caso a soma desses valores seja igual ao tamanho da mensagem recebida (contando os espaços), será considerada como código morse. Caso contrário, será considera como texto. 
3. Tradução: identificando o tipo de mensagem, será chamada a respectiva função de tradução, que irá ser traduzida de letra por letra. Há duas possibilidades:
a) Tradução de txt para morse: traduzição realizada de letra por letra, através de um laço de repetição que percorre a mensagem original, "substituindo" as letras originais por letras em código morse (na realidade, é criada outra variável para armazenar a mensagem traduzida). É adicionado um espaço ao final de cada letra, e um espaço extra no final de cada espaço da mensagem original:
b) Tradução de morse para txt: Nesse caso, foi necessário separar a string de uma forma diferente do normal, já que ao separar a string com split, todos os espaços, únicos ou duplos, são enviados como único, sendo a mensagem enviada, e consequentemente recebida, sem os espaços duplos simbolizando o fim da palavra. Por esse motivo, foi necessário utilizar um outro recurso parecido, chamado de re.split, para que os espaços duplos ficassem salvos de alguma forma na mensagem, perimitindo que o mensagem fosse traduzida da forma correta.
  
## Quanto à saída da mensagem
- Abaixo há uma descrição das saídas esperadas por cada aplicação
- Obs.: As palavras ou frases escritas entre aspas duplas são as escritas de forma literal no código
  
#### 1. No emissor da mensagem, será impresso, em uma única linha:
1. Seta para a direita ("→")
2. "Sent "
3. 'Palavra chave' (impresso com aspas simples)
4. Dois pontos (":"), separando a palavra chave da mensagem enviada
5. Mensagem enviada
  
#### 2. No receptor da mensagem, será impresso, em uma única linha:
1. "Received: "
2. Mensagem recebida
3. Seta para a direita ("→")
4. "Tranlation: "
5. Tradução da mensagem recebida
  
## Evolução do produto
A primeira coisa a ser feita é mudar a forma como as letras são identificadas e traduzidas. Atualmente, existe um dicionário com uma quantidade maior do que o adequado. Considerando que isso está em um arquivo separado e, só tem isso, não é muito difícil de entender, mas não é a melhor das ideias colocar uma grande quantidade de ifs seguidos. Reduzir essa quantidade sem alterar o resultado aumentaria razoavelmente a qualidade do código, apesar de atualmente não estar prejudicando. 

Outro detalhe que poderia ser implementado, seria uma autenticação da chave, para que isso funcione como uma espécie de login e senha, tornando o envio e recebimento das mensagens mais seguros, evitando que outras pessoas indesejadas visualizem determinada mensagem.

Em terceiro lugar, organizaria o código de forma um pouco mais eficiente, de forma a facilitar a identificação e visualização do arquivos. Isso não chega a ser necessário nesse momento, porque não há uma grande quantidade de arquivos, mas caso haja intenção de expandi-lo, colocar tudo em um único diretório pode não ser uma boa ideia, por dificultar o desenvolvimento da solução.
