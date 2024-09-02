import os
import time
import requests
import threading
from colored import fore as cf

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_terminal_color():
    if os.name == 'nt':
        os.system('color')
    else:
        print("\033[0m", end='')

def load_banner(filename):
    with open(f'ascii_banners/{filename}', 'r', encoding='utf-8') as file:
        return file.read()

def print_banner(filename, style='red'):
    banner = load_banner(filename)
    if style == 'rainbow':
        rainbow_colors = [cf('red'), cf('yellow'), cf('green'), cf('cyan'), cf('blue'), cf('magenta')]
        for i, line in enumerate(banner.splitlines()):
            print(rainbow_colors[i % len(rainbow_colors)] + line)
    else:
        print(cf('red') + banner)

def typewriter_effect(text, delay=0.05, color=cf('cyan')):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def send_message(webhook_url, message, spam_count):
    for _ in range(spam_count):
        try:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                print(cf('green') + "✔️ Mensagem enviada.")
            elif response.status_code == 429:
                print(cf('yellow') + "⚠️ Rate limit atingido. Esperando...")
                time.sleep(5)
            elif response.status_code == 401:
                print(cf('red') + "❌ Falha 401: Não autorizado.")
            else:
                print(cf('red') + f"❌ Falha: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(cf('red') + f"❌ Erro na requisição: {e}")
        time.sleep(0.5)

def send_messages(webhook_urls, message, spam_count):
    threads = []
    for webhook_url in webhook_urls:
        thread = threading.Thread(target=send_message, args=(webhook_url, message, spam_count))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    print(cf('green') + "✅ Todos os webhooks foram processados.")
    input(cf('white') + "\nPressione Enter para voltar ao menu...")
    clear_screen()
    print_banner('banner2.txt', style='rainbow')

def list_webhooks():
    clear_screen()
    print_banner('banner2.txt', style='rainbow')
    if not os.path.exists('webhooks.txt'):
        print(cf('red') + "Arquivo de webhooks não encontrado.")
        input(cf('white') + "Pressione Enter para voltar ao menu...")
        clear_screen()
        return
    
    with open('webhooks.txt', 'r', encoding='utf-8') as file:
        webhooks = file.readlines()
    
    if not webhooks:
        print(cf('red') + "Nenhum webhook encontrado.")
        input(cf('white') + "Pressione Enter para voltar ao menu...")
        clear_screen()
        return
    
    print(cf('cyan') + "Webhooks atuais:")
    for i, webhook in enumerate(webhooks):
        print(cf('cyan') + f"[{i + 1}] {webhook.strip()}")
    
    input(cf('white') + "Pressione Enter para voltar ao menu...")
    clear_screen()
    print_banner('banner2.txt', style='rainbow')

def verify_webhooks():
    clear_screen()
    print_banner('banner2.txt', style='rainbow')
    if not os.path.exists('webhooks.txt'):
        print(cf('red') + "Arquivo de webhooks não encontrado.")
        input(cf('white') + "Pressione Enter para voltar ao menu...")
        clear_screen()
        return
    
    with open('webhooks.txt', 'r', encoding='utf-8') as file:
        webhooks = file.readlines()
    
    if not webhooks:
        print(cf('red') + "Nenhum webhook encontrado.")
        input(cf('white') + "Pressione Enter para voltar ao menu...")
        clear_screen()
        return
    
    print(cf('cyan') + "Verificando webhooks...")
    def verify_webhook(webhook_url):
        try:
            response = requests.get(webhook_url.strip())
            if response.status_code == 200:
                print(cf('green') + f"✔️ Webhook {webhook_url.strip()} está funcionando.")
            elif response.status_code == 401:
                print(cf('red') + f"❌ Webhook {webhook_url.strip()} retornou status 401: Não autorizado.")
            else:
                print(cf('red') + f"❌ Webhook {webhook_url.strip()} retornou status {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(cf('red') + f"❌ Erro ao verificar o webhook {webhook_url.strip()}: {e}")

    threads = []
    for webhook_url in webhooks:
        thread = threading.Thread(target=verify_webhook, args=(webhook_url,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    input(cf('white') + "Pressione Enter para voltar ao menu...")
    clear_screen()
    print_banner('banner2.txt', style='rainbow')

def main():
    clear_screen()
    print_banner('banner1.txt', style='red')
    
    typewriter_effect("Bem-vindo ao Foltz WBS! Prepare-se para uma experiência incrível\nCriado por Foltz\n https://github.com/foltzbr.", color=cf('white'))
    time.sleep(3)
    clear_screen()
    print_banner('banner2.txt', style='rainbow')

    while True:
        print(cf('yellow') + """
[1] Adicionar Webhook
[2] Deletar Webhook
[3] Listar Webhooks
[4] Verificar Webhooks
[5] Enviar Mensagens
[6] Sair
""")

        choice = input(cf('white') + "Escolha uma opção: ").strip()

        if choice == '1':
            clear_screen()
            print(cf('magenta') + "🔧 Adicionar Webhook 🔧")
            print_banner('banner2.txt', style='rainbow')
            url = input(cf('white') + "Digite a URL do webhook (ou pressione Enter para voltar): ").strip()
            if url:
                with open('webhooks.txt', 'a', encoding='utf-8') as file:
                    file.write(f"{url}\n")
                print(cf('green') + "Webhook adicionado.")
                time.sleep(2)
            else:
                print(cf('yellow') + "Nenhuma URL inserida. Voltando ao menu...")
                time.sleep(2)
                clear_screen()
                print_banner('banner2.txt', style='rainbow')

        elif choice == '2':
            clear_screen()
            print(cf('magenta') + "🗑️ Deletar Webhook 🗑️")
            print_banner('banner2.txt', style='rainbow')
            if not os.path.exists('webhooks.txt'):
                print(cf('red') + "Arquivo de webhooks não encontrado.")
                time.sleep(2)
                clear_screen()
                print_banner('banner2.txt', style='rainbow')
                continue

            with open('webhooks.txt', 'r', encoding='utf-8') as file:
                webhooks = file.readlines()
            
            if not webhooks:
                print(cf('red') + "Nenhum webhook para deletar.")
                time.sleep(2)
                clear_screen()
                print_banner('banner2.txt', style='rainbow')
                continue
            
            print(cf('cyan') + "Selecione o webhook para deletar:")
            for i, webhook in enumerate(webhooks):
                print(cf('cyan') + f"[{i + 1}] {webhook.strip()}")
            
            try:
                delete_index = input(cf('white') + "Digite o número do webhook para deletar (ou pressione Enter para voltar): ").strip()
                if delete_index:
                    delete_index = int(delete_index) - 1
                    if 0 <= delete_index < len(webhooks):
                        del webhooks[delete_index]
                        with open('webhooks.txt', 'w', encoding='utf-8') as file:
                            file.writelines(webhooks)
                        print(cf('green') + "Webhook deletado.")
                    else:
                        print(cf('red') + "Número inválido.")
                else:
                    print(cf('yellow') + "Nenhum número inserido. Voltando ao menu...")
            except ValueError:
                print(cf('red') + "Entrada inválida.")
            time.sleep(2)
            clear_screen()
            print_banner('banner2.txt', style='rainbow')

        elif choice == '3':
            list_webhooks()

        elif choice == '4':
            verify_webhooks()

        elif choice == '5':
            clear_screen()
            print(cf('magenta') + "📤 Enviar Mensagens 📤")
            print_banner('banner2.txt', style='rainbow')
            if not os.path.exists('webhooks.txt'):
                print(cf('red') + "Arquivo de webhooks não encontrado.")
                input(cf('white') + "Pressione Enter para voltar ao menu...")
                clear_screen()
                continue

            with open('webhooks.txt', 'r', encoding='utf-8') as file:
                webhooks = file.readlines()
            
            if not webhooks:
                print(cf('red') + "Nenhum webhook encontrado.")
                input(cf('white') + "Pressione Enter para voltar ao menu...")
                clear_screen()
                continue

            message = input(cf('white') + "Digite a mensagem para enviar: ").strip()
            if not message:
                print(cf('red') + "Mensagem não pode estar vazia.")
                time.sleep(2)
                clear_screen()
                print_banner('banner2.txt', style='rainbow')
                continue

            try:
                spam_count = int(input(cf('white') + "Digite o número de vezes para spam: ").strip())
                if spam_count < 1:
                    print(cf('red') + "Número de vezes deve ser maior que 0.")
                    continue
            except ValueError:
                print(cf('red') + "Entrada inválida.")
                continue

            send_messages(webhooks, message, spam_count)

        elif choice == '6':
            print(cf('red') + "Saindo...")
            time.sleep(1)
            break

        else:
            print(cf('red') + "Opção inválida.")
            time.sleep(1)
            clear_screen()
            print_banner('banner2.txt', style='rainbow')

if __name__ == "__main__":
    main()
