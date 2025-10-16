# 🧠 Dynamic Programming – Controle de Insumos

## 📋 Contexto
Nas unidades de diagnóstico, o consumo diário de insumos (reagentes e descartáveis) não é registrado com precisão, dificultando o controle de estoque e a previsão de reposição.  
Este projeto aplica **Programação Dinâmica** e **estruturas de dados** para melhorar a visibilidade do consumo e reduzir desperdícios.

---

## ⚙️ Estrutura do Projeto

### 🧪 Função `gerar_consumo()`
Responsável por simular o consumo diário de insumos, criando dados fictícios que representam a quantidade e a validade de cada item utilizado ao longo dos dias.  
Esses dados alimentam o sistema para prever futuras reposições e controlar o estoque.

---

### 🧾 Estruturas: `fila_consumo` e `pilha_consumo`
- **`fila_consumo` (Fila - FIFO):** armazena o histórico de consumo em ordem cronológica, representando o uso dos insumos dia a dia.  
- **`pilha_consumo` (Pilha - LIFO):** mantém o histórico em ordem inversa, útil para consultar rapidamente os últimos consumos registrados.

Essas estruturas organizam o fluxo de entrada e saída de insumos, facilitando o controle de utilização.

---

### 🔍 Funções de Busca
- **`busca_sequencial()`**: percorre todos os registros até encontrar o insumo desejado. Ideal para listas pequenas ou não ordenadas.  
- **`busca_binaria()`**: busca eficiente em listas ordenadas, reduzindo o número de comparações necessárias para localizar um insumo.

Essas buscas otimizam a consulta de reagentes ou descartáveis específicos dentro do sistema.

---

### 🔁 Funções de Ordenação
- **`merge_sort()`**: organiza os insumos com base na quantidade consumida. Isso ajuda a identificar quais itens são mais utilizados e requerem reposição com maior frequência.  
- **`quick_sort()`**: ordena os insumos de acordo com a validade, permitindo priorizar o uso daqueles que estão mais próximos do vencimento.

Esses algoritmos garantem eficiência e reduzem desperdício de materiais.

---

### 📊 Função `relatorio()`
Reúne todas as informações do sistema e apresenta:
- O histórico de consumo na fila e na pilha;  
- Resultados das buscas realizadas;  
- Listas de insumos ordenadas por quantidade e validade.  

Essa função oferece ao gestor uma visão consolidada do consumo e auxilia na tomada de decisão sobre reposições.

---

## 🧩 Aplicação de Programação Dinâmica
O conceito de **Programação Dinâmica** aparece na reutilização de resultados intermediários, como listas ordenadas e resultados de busca, evitando cálculos repetidos e otimizando o desempenho do sistema.  
Isso torna o processo de controle de estoque mais eficiente e inteligente.

---

## 🧾 Integrantes
Integrantes:
- Arthur Galvão Alves - RM554462
- Felipe Braunstein e Silva - RM554483
- Felipe do Nascimento Fernandes - RM554598
- Henrique Ignacio Bartalo - 555274
- Gustavo Henrique Martins - RM556956
