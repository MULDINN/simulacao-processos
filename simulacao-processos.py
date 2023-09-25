import random
import time

# Tabela de processos

processes = []
for pid in range(10):
    processes.append({
        "pid": pid,
        "tp": 0,
        "cp": 0,
        "ep": "pronto",
        "nes": 0,
        "n_cpu": 0
    })

# Tempo de execução de cada processo

exec_times = {
    0: 10000,
    1: 5000,
    2: 7000,
    3: 3000,
    4: 3000,
    5: 8000,
    6: 2000,
    7: 5000,
    8: 4000,
    9: 10000
}

# Quantum de execução

quantum = 1000

# Função para gerar uma operação de E/S

def gerar_operacao_es():
    return random.random() <= 0.05

# Função para realizar uma troca de contexto

def trocar_contexto(processo):
    # Atualiza os dados do processo

    processo["tp"] += quantum
    processo["cp"] = processo["tp"] + 1
    processo["ep"] = "pronto"
    processo["nes"] += 0 if processo["ep"] == "pronto" else 1
    processo["n_cpu"] += 1 if processo["ep"] == "executando" else 0

    # Imprime os dados do processo

    print(f"Processo {processo['pid']}: {processo['ep']} -> {processo['ep']}")
    print(f"TP: {processo['tp']}")
    print(f"CP: {processo['cp']}")
    print(f"NES: {processo['nes']}")
    print(f"N_CPU: {processo['n_cpu']}")

# Função para executar um processo

def executar_processo(processo):
    # Verifica se o processo deve realizar uma operação de E/S

    if gerar_operacao_es():
        processo["ep"] = "bloqueado"
        print(f"Processo {processo['pid']}: {processo['ep']} -> BLOQUEADO")
        return

    # Verifica se o processo terminou sua execução

    if processo["tp"] >= exec_times[processo["pid"]]:
        processo["ep"] = "terminado"
        print(f"Processo {processo['pid']}: {processo['ep']} -> TERMINADO")
        return

    # Executa um ciclo do processo

    processo["tp"] += 1

# Função principal

def main():
    # Inicializa o sistema operacional

    processo_atual = processes.pop(0)
    print(f"Processo {processo_atual['pid']}: PRONTO -> EXECUTANDO")

    # Loop principal do sistema operacional

    while True:
        # Verifica se o processo atual terminou sua execução

        if processo_atual["ep"] == "terminado":
            processes.append(processo_atual)
            processo_atual = processes.pop(0) if processes else None
            continue

        # Executa um ciclo do processo atual

        executar_processo(processo_atual)

        # Troca de contexto, se necessário

        if processo_atual["ep"] == "pronto":
            trocar_contexto(processo_atual)
            processo_atual = processes.pop(0) if processes else None

# Chama a função principal

main()
