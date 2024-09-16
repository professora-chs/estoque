import tkinter as tk
from tkinter import ttk, messagebox

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
    for item in tree.get_children():
        tree.delete(item)
    for nome, info in estoque.items():
        tree.insert('', 'end', values=(nome, info['quantidade'], f"R${info['preco']:.2f}"))


# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo de Estoque")
root.geometry("600x400")

# Frame para entradas
frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.grid(row=0, column=0, sticky="ew")

# Campos de entrada
ttk.Label(frame_inputs, text="Nome do Item:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nome = ttk.Entry(frame_inputs, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_quantidade = ttk.Entry(frame_inputs, width=30)
entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Preço Unitário:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_preco = ttk.Entry(frame_inputs, width=30)
entry_preco.grid(row=2, column=1, padx=5, pady=5)

# Frame para botões
frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.grid(row=1, column=0, sticky="ew")

# Botões de ações
ttk.Button(frame_buttons, text="Adicionar Item", command=adicionar_item).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_buttons, text="Remover Item", command=remover_item).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_buttons, text="Atualizar Item", command=atualizar_item).grid(row=0, column=2, padx=5, pady=5)

# Frame para listagem
frame_list = ttk.Frame(root, padding="10")
frame_list.grid(row=2, column=0, sticky="nsew")

# Lista de estoque com árvore (treeview)
tree = ttk.Treeview(frame_list, columns=('Nome', 'Quantidade', 'Preço'), show='headings', height=8)
tree.heading('Nome', text='Nome')
tree.heading('Quantidade', text='Quantidade')
tree.heading('Preço', text='Preço')
tree.grid(row=0, column=0, sticky="nsew")

# Barra de rolagem para a lista
scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configuração para redimensionamento
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Inicializa a interface gráfica
atualizar_lista()
root.mainloop()
