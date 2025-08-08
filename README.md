# 📊 Dashboard de Nascimentos Vivos - Ceará

Um dashboard interativo criado com Dash e Plotly para visualizar dados sintéticos de nascimentos vivos em diferentes cidades do Ceará.

## 🚀 Características

- **Dados Sintéticos Realistas**: Geração de dados de nascimentos para 5 cidades do Ceará (2010-2023)
- **Gráficos Interativos**: Gráficos de linha com animação e hover detalhado
- **Filtros Dinâmicos**: Seleção de cidades e período temporal
- **Estatísticas em Tempo Real**: Cards com métricas atualizadas dinamicamente
- **Design Responsivo**: Interface moderna com Bootstrap
- **Animações**: Transições suaves e efeitos visuais

## 📋 Pré-requisitos

- Python 3.7+
- pip

## 🛠️ Instalação

1. Clone ou baixe os arquivos do projeto
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🎯 Como Executar

1. Execute o aplicativo:

```bash
python app.py
```

2. Abra seu navegador e acesse:
   ```
   http://localhost:8050
   ```

## 📊 Funcionalidades

### Gráfico de Tendência
- Linhas de evolução temporal para cada cidade
- Hover com informações detalhadas
- Animações de transição
- Legendas interativas

### Gráfico de Comparação
- Barras comparativas por cidade
- Médias calculadas dinamicamente
- Cores diferenciadas por cidade

### Painel de Estatísticas
- Total de nascimentos
- Média de nascimentos
- Valores máximo e mínimo
- Atualização em tempo real

### Controles Interativos
- Dropdown para seleção de cidades
- Slider para definição do período
- Filtros aplicados em todos os gráficos

## 🎨 Tecnologias Utilizadas

- **Dash**: Framework web para aplicações analíticas
- **Plotly**: Biblioteca para gráficos interativos
- **Bootstrap**: Framework CSS para design responsivo
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação numérica

## 📈 Dados Sintéticos

O dashboard utiliza dados sintéticos gerados com as seguintes características:

- **Cidades**: Fortaleza, Caucaia, Juazeiro do Norte, Maracanaú, Sobral
- **Período**: 2010-2023
- **Tendências**: Cada cidade possui uma tendência base diferente
- **Variações**: Inclui variação sazonal e ruído aleatório para realismo

## 🔧 Personalização

Para modificar os dados ou adicionar novas funcionalidades:

1. Edite a função `generate_synthetic_data()` em `app.py`
2. Adicione novas cidades ou modifique as tendências
3. Personalize cores e estilos nos callbacks
4. Adicione novos tipos de gráficos conforme necessário

## 📱 Responsividade

O dashboard é totalmente responsivo e funciona bem em:
- Desktops
- Tablets
- Smartphones

## 🎯 Próximos Passos

Possíveis melhorias futuras:
- Adicionar mais tipos de gráficos (pizza, scatter, etc.)
- Implementar exportação de dados
- Adicionar mais filtros (por região, faixa etária, etc.)
- Integração com APIs de dados reais
- Dashboard em tempo real com atualizações automáticas
