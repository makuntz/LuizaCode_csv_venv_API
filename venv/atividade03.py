
#===========================================
# Persistencia / Repositorio
#===========================================

MEMORIA_MUSICAS = []

def persistencia_musica_salvar(nova_musica):
    codigo_nova_musica = len(MEMORIA_MUSICAS) + 1
    # Ajuste na persistencia (colocar id?)
    nova_musica["codigo"] = codigo_nova_musica
    # Salvar na persistencia/repositorio
    MEMORIA_MUSICAS.append(nova_musica)
    return nova_musica


def persistencia_musica_pesquisar_todas():
    lista_musicas = list(MEMORIA_MUSICAS)
    return lista_musicas


def persistencia_pesquisar_pelo_codigo(codigo):
    musica_procurada = None
    for musica in MEMORIA_MUSICAS:
        if musica["codigo"] == codigo:
            musica_procurada = musica
            # Pode parar o 'for' e sair dele
            break 
    return musica_procurada

#===========================================
# Regras / Casos de uso
#===========================================

def regras_musica_cadastrar(nova_musica):
    # TODO validar a nova musica
    # regras_musica_validar_nova_musica(nova_musica)
    nova_musica = persistencia_musica_salvar(nova_musica)
    return nova_musica


def regras_musica_pesquisar_todas():
    return persistencia_musica_pesquisar_todas()

def regras_musica_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo(codigo)



#===========================================
# API Rest / Controlador
#===========================================

# -------- rotas / caminhos / salas
import fastapi
import pydantic
from typing import Optional
aplicacao_web = fastapi.FastAPI()

@aplicacao_web.get("/")
def rota_raiz():
    return {
        "ok": True,
        "versao": "Fase1"
    }
    
class NovaMusica(pydantic.BaseModel):
    nome: str
    artista: str
    tempo: Optional[int]
    

@aplicacao_web.post("/musicas")
def rota_musica_cadastrada(nova_musica: NovaMusica):
    print("Registrando nova musica: ", nova_musica.dict())
    nova_musica = regras_musica_cadastrar(nova_musica.dict())
    return nova_musica
    

@aplicacao_web.get("/musicas")
def rota_musica_pesquisar_todas():
    return regras_musica_pesquisar_todas()


@aplicacao_web.get("/musicas/{codigo}")
def rota_musica_pesquisar_pelo_codigo(codigo: int):
    print("consulta pleo codigo: ", codigo)
    return regras_musica_pesquisar_pelo_codigo(codigo)

