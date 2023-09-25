# simulacao-processos

Criar uma aplicação em (Qualquer Linguagem),  para simular a mudança de estados dos processos num SO. Nesse sistema operacional, estão em execução 10 processos que são colocados para a execução em ordem do seu PID (Identificador de processo que vai de 0 a 9) com tempo de duração distintos. 

Somente um processo por vez pode estar no estado de EXECUTANDO. O SO definiu um Quantum de execução para cada processo de 1000 ciclos. Em cada ciclo o processo tem 5% de chances de realizar uma operação de E/S, ficando então bloqueado. Uma vez que ele realizar uma operação de E/S, na sua próxima vez, ele terá 30% de chances para sair do estado de Bloqueado e ir para o estado de Pronto. 

Caso o quantum do processo termine sem ele realizar uma operação de E/S (término dos 1000 ciclos), o processo sofrerá uma Troca de Contexto, modificando seu estado de executando  para Pronto.

Cada processo possui como dados: IDENTIFICADOR DE PROCESSO (PID), TEMPO DE PROCESSAMENTO (TP), CONTADOR DE PROGRAMA (CP), ESTADO DO PROCESSO (EP), NÚMERO DE VEZES QUE REALIZOU UMA OPERAÇÃO DE E/S (NES) e NÚMERO DE VEZES QUE USOU A CPU (N_CPU)  Logo, sempre que um processo sofrer uma Troca de Contexto, esses dados devem ser  guardados na Tabela de Processos (gravar os dados num arquivo TXT e atualizar esses dados em cada troca de contexto).

Cada vez que um processo passar do estado de PRONTO para EXECUTANDO, os dados do processo devem ser restaurados.

O tempo de execução de cada processo segue a seguinte Tabela:

PID     Tempo de Execução para terminar a execução (Em ciclos)

0          10000

1          5000

2          7000

3          3000

4          3000

5          8000

6          2000

7          5000

8          4000

9          10000
