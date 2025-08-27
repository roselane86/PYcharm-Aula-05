def imprimir(produtos):

    print("****************** Produtos Cadastrados *************************")
    for prod in produtos:
        produto = prod["produto"]
        marca = prod["marca"]
        print(f"Produto : {produto} - Marca : {marca}")

produtos = [
    {"produto":"Tv 50 polegadas","marca":"Samsung"},
    {"produto":"Micro-ondas","marca":"Panasonic"},
    {"produto":"Iphone 15 pro max","marca":"Apple"},
    {"produto":"Smartphone redmi note 13","marca":"Xiaomi"},
    {"produto":"Lavadora 10 kg","marca":"Brastemp"}
]

imprimir(produtos)
