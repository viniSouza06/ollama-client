import requests

OLLAMA_URL = "http://ollama.eastus.cloudapp.azure.com:11434/api/generate"
MODEL = "phi3:mini"

def enviar_prompt(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("response", "Nenhuma resposta recebida.")
    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com a API: {e}"

def main():
    print("🧠 Cliente Ollama - Modelo phi3:mini")
    while True:
        prompt = input("\nDigite seu prompt (ou 'sair' para encerrar): ")
        if prompt.lower() == "sair":
            break
        resposta = enviar_prompt(prompt)
        print(f"\n💬 Resposta da IA:\n{resposta}")

if __name__ == "__main__":
    main()
