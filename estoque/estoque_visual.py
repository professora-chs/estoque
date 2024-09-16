import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os itens do estoque
estoque = {}


def adicionar_item():
    """Adiciona um novo item ao estoque."""
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit():
        quantidade = int(quantidade)
        preco = float(preco)
        if nome in estoque:
            estoque[nome]['quantidade'] += quantidade
            messagebox.showinfo("Sucesso", f"{quantidade} unidades adicionadas ao item '{nome}'.")
        else:
            estoque[nome] = {'quantidade': quantidade, 'preco': preco}
            messagebox.showinfo("Sucesso", f"Item '{nome}' adicionado ao estoque.")
        atualizar_lista()
    else:
        messagebox.showwarning("Erro", "Por favor, insira valores válidos.")


def remover_item():
    """Remove um item do estoque."""
    nome = entry_nome.get()

    if nome in estoque:
        del estoque[nome]
        messagebox.showinfo("Sucesso", f"Item '{nome}' removido do estoque.")
        atualizar_lista()
    else:
        messagebox.showwarning("Erro", f"Item '{nome}' não encontrado no estoque.")


def atualizar_item():
    """Atualiza a quantidade e o preço de um item."""
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    if nome in estoque and quantidade.isdigit() and preco.replace('.', '', 1).isdigit():
        estoque[nome] = {'quantidade': int(quantidade), 'preco': float(preco)}
        messagebox.showinfo("Sucesso", f"Item '{nome}' atualizado.")
        atualizar_lista()
    else:
        messagebox.showwarning("Erro", "Por favor, insira um item existente e valores válidos.")


def atualizar_lista():
    """Atualiza a lista de itens na interface."""
    listbox_estoque.delete(0, tk.END)
    for nome, info in estoque.items():
        listbox_estoque.insert(tk.END,
                               f"Item: {nome} | Quantidade: {info['quantidade']} | Preço: R${info['preco']:.2f}")


# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo de Estoque")

# Campos de entrada
tk.Label(root, text="Nome do Item:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Quantidade:").grid(row=1, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=1, column=1)

tk.Label(root, text="Preço Unitário:").grid(row=2, column=0)
entry_preco = tk.Entry(root)
entry_preco.grid(row=2, column=1)

# Botões de ações
tk.Button(root, text="Adicionar Item", command=adicionar_item).grid(row=3, column=0)
tk.Button(root, text="Remover Item", command=remover_item).grid(row=3, column=1)
tk.Button(root, text="Atualizar Item", command=atualizar_item).grid(row=4, column=0)

# Listbox para exibir o estoque
listbox_estoque = tk.Listbox(root, width=50)
listbox_estoque.grid(row=5, column=0, columnspan=2)

# Inicializa a interface gráfica
atualizar_lista()
root.mainloop()
