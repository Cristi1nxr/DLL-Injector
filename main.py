from pyinjector import inject

pid = int (input ("Primul pas, introdu PID-ul fisierului: "))
dll = input("Al doilea pas, introdu calea catre DLL: ")

inject(pid, dll)

print("Injectat!")