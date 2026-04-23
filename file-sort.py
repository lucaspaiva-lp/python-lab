import os
import shutil
from pathlib import Path

# Configuração
BASE_DIR = Path('.')
SOURCE_DIR = BASE_DIR / 'A-Z'  # De onde ele deve ler os arquivos
DRY_RUN = False  # Mude para False somente após rodar a simulação e validar o output

# A ordem importa: o script para na primeira correspondência encontrada.
mapping = {
    # 1. Conflitos de nomenclatura (ex: Node/JS vs Java puro)
    'node': '02_backend_programacao',
    'mean': '02_backend_programacao',
    'meteor': '02_backend_programacao',
    'javascript': '05_frontend_mobile',
    'java ': '02_backend_programacao',
    'java-': '02_backend_programacao',
    'java_': '02_backend_programacao',

    # 2. Hardware, Embarcados e Fundamentos
    'arduino': '06_fundamentos_hardware',
    'msp430': '06_fundamentos_hardware',
    'pic microcontroller': '06_fundamentos_hardware',
    'embedded': '06_fundamentos_hardware',
    'circuit': '06_fundamentos_hardware',
    'eletrônica': '06_fundamentos_hardware',
    'microcontroller': '06_fundamentos_hardware',
    'sensors': '06_fundamentos_hardware',
    'arquitetura e organização': '06_fundamentos_hardware',
    'organização estruturada': '06_fundamentos_hardware',
    'organização de computadores': '06_fundamentos_hardware',
    'compiladores': '06_fundamentos_hardware',
    'sistemas operacionais': '06_fundamentos_hardware',
    'calculo': '06_fundamentos_hardware',
    'cálculo': '06_fundamentos_hardware',
    'inteligência artificial': '06_fundamentos_hardware',
    'computação quântica': '06_fundamentos_hardware',
    'opengl': '06_fundamentos_hardware',

    # 3. Bancos de Dados e Dados
    'sql': '04_bancos_dados',
    'banco de dados': '04_bancos_dados',
    'bancos de dados': '04_bancos_dados',
    'oracle': '04_bancos_dados',
    'mongodb': '04_bancos_dados',
    'redis': '04_bancos_dados',
    'elasticsearch': '04_bancos_dados',
    'big data': '04_bancos_dados',
    'data science': '04_bancos_dados',
    'mineração': '04_bancos_dados',

    # 4. Infra, DevOps, Redes e Segurança
    'docker': '03_infra_devops',
    'linux': '03_infra_devops',
    'ubuntu': '03_infra_devops',
    'shell script': '03_infra_devops',
    'devops': '03_infra_devops',
    'jenkins': '03_infra_devops',
    'git': '03_infra_devops',
    'redes': '03_infra_devops',
    'protocolos': '03_infra_devops',
    'segurança': '03_infra_devops',
    'seguranca': '03_infra_devops',
    'crypto': '03_infra_devops',
    'hacker': '03_infra_devops',
    'windows server': '03_infra_devops',
    'virtualbox': '03_infra_devops',
    'direito-digital': '03_infra_devops',
    'dados-pessoais': '03_infra_devops',

    # 5. Frontend, Mobile e UI/UX
    'html': '05_frontend_mobile',
    'css': '05_frontend_mobile',
    'sass': '05_frontend_mobile',
    'front-end': '05_frontend_mobile',
    'frontend': '05_frontend_mobile',
    'jquery': '05_frontend_mobile',
    'react': '05_frontend_mobile',
    'ux': '05_frontend_mobile',
    'mobile': '05_frontend_mobile',
    'ios': '05_frontend_mobile',
    'android': '05_frontend_mobile',
    'iphone': '05_frontend_mobile',
    'ipad': '05_frontend_mobile',
    'windows phone': '05_frontend_mobile',
    'photoshop': '05_frontend_mobile',
    'lightroom': '05_frontend_mobile',
    'computação gráfica': '05_frontend_mobile',

    # 6. Arquitetura, Eng. de Software e Ágil
    'arquitetura': '01_arquitetura_software',
    'design pattern': '01_arquitetura_software',
    'clean code': '01_arquitetura_software',
    'codigo limpo': '01_arquitetura_software',
    'solid': '01_arquitetura_software',
    'tdd': '01_arquitetura_software',
    'test-driven': '01_arquitetura_software',
    'test driven': '01_arquitetura_software',
    'rspec': '01_arquitetura_software',
    'cucumber': '01_arquitetura_software',
    'engenharia de software': '01_arquitetura_software',
    'agile': '01_arquitetura_software',
    'scrum': '01_arquitetura_software',
    'extreme programming': '01_arquitetura_software',
    'startup': '01_arquitetura_software',
    'lean enterprise': '01_arquitetura_software',
    'domain-driven': '01_arquitetura_software',
    'soa ': '01_arquitetura_software',
    'apaixonado': '01_arquitetura_software',
    'mestre programador': '01_arquitetura_software',
    'fragmentos': '01_arquitetura_software',
    'direto ao ponto': '01_arquitetura_software',

    # 7. Backend e Lógica de Programação (Catch-all)
    'java': '02_backend_programacao',
    'spring': '02_backend_programacao',
    'jpa': '02_backend_programacao',
    'jsf': '02_backend_programacao',
    'cdi': '02_backend_programacao',
    'vraptor': '02_backend_programacao',
    'python': '02_backend_programacao',
    'ruby': '02_backend_programacao',
    'rails': '02_backend_programacao',
    'php': '02_backend_programacao',
    'laravel': '02_backend_programacao',
    'zend': '02_backend_programacao',
    'c#': '02_backend_programacao',
    'asp.net': '02_backend_programacao',
    'go ': '02_backend_programacao',
    'algoritmo': '02_backend_programacao',
    'algorithms': '02_backend_programacao',
    'lógica': '02_backend_programacao',
    'logica': '02_backend_programacao',
    'programação': '02_backend_programacao',
    'programacao': '02_backend_programacao',

    # 8. Negócios, Literatura e Diversos
    'contabilidade': '07_negocios_literatura',
    'ação': '07_negocios_literatura',
    'investimento': '07_negocios_literatura',
    'vender': '07_negocios_literatura',
    'produtividade': '07_negocios_literatura',
    'estudar': '07_negocios_literatura',
    'frankenstein': '07_negocios_literatura',
    'metamorphosis': '07_negocios_literatura',
    'orwell': '07_negocios_literatura',
    '1984': '07_negocios_literatura',
    'animal farm': '07_negocios_literatura',
    'emma': '07_negocios_literatura',
    'capitães': '07_negocios_literatura',
    'blindness': '07_negocios_literatura',
    'pride': '07_negocios_literatura',
    'littleprince': '07_negocios_literatura',
    'dorian': '07_negocios_literatura',
    'jekyll': '07_negocios_literatura',
    'english': '07_negocios_literatura',
    'nações': '07_negocios_literatura',
    'servidao': '07_negocios_literatura',
    'games': '07_negocios_literatura',
    'mochileiro': '07_negocios_literatura',
    
    # Adições para os sobreviventes
    'gestão de produtos': '01_arquitetura_software',
    'sprint': '01_arquitetura_software',
    'design_patterns': '01_arquitetura_software',
    'markdown': '01_arquitetura_software',
    
    'rest': '02_backend_programacao',
    'vba': '02_backend_programacao',
    'tkinter': '02_backend_programacao',
    
    'windows': '03_infra_devops',
    'azure': '03_infra_devops',
    'rede': '03_infra_devops',
    'nuvem': '03_infra_devops',
    'security': '03_infra_devops',
    '27': '03_infra_devops',
    
    'seo': '07_negocios_literatura',
    'minha_acao': '07_negocios_literatura',
    'full stack': '07_negocios_literatura',
    'green gables': '07_negocios_literatura',
    'lucy maud': '07_negocios_literatura',
    
    'wd_': '05_frontend_mobile',
    'responsivo': '05_frontend_mobile',
    'jogos 3d': '05_frontend_mobile',
    
    'compilladores': '06_fundamentos_hardware', 
    'manutenção': '06_fundamentos_hardware',
    'ardui': '06_fundamentos_hardware',
    'introduction-to-embedded-systems': '06_fundamentos_hardware',
    'architecture-patterns': '01_arquitetura_software',
    'clean architecture': '01_arquitetura_software',
    'pragmatic programmer': '01_arquitetura_software',
    
    'data-intensive': '04_bancos_dados',
    'entityrelations': '04_bancos_dados',
    'sql antipatterns': '04_bancos_dados',
    
    'crash course': '02_backend_programacao',
    
    'phoenix project': '03_infra_devops',
    
    'english grammar': '07_negocios_literatura',
}

def organizar():
    # Verifica se a pasta A-Z existe
    if not SOURCE_DIR.exists():
        print(f"Erro: A pasta '{SOURCE_DIR}' não foi encontrada.")
        return

    for arquivo in SOURCE_DIR.iterdir():
        # Foca apenas em arquivos (ignora subpastas dentro de A-Z)
        if arquivo.is_file() and arquivo.suffix.lower() in ['.pdf', '.epub', '.ppt', '.pptx']:
            nome_lower = arquivo.name.lower()
            movido = False
            
            for keyword, pasta in mapping.items():
                if keyword in nome_lower:
                    destino_dir = BASE_DIR / pasta
                    # Cria a pasta no nível de 'books/' se não existir
                    destino_dir.mkdir(exist_ok=True) 
                    
                    destino_arquivo = destino_dir / arquivo.name
                    
                    if DRY_RUN:
                        print(f"[SIMULAÇÃO] Mover '{arquivo.name}' -> {pasta}/")
                    else:
                        shutil.move(str(arquivo), str(destino_arquivo))
                    movido = True
                    break
            
            if not movido:
                print(f"[!] Sem destino para: '{arquivo.name}'")

if __name__ == "__main__":
    organizar()