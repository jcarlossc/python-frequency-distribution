{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8898b754",
   "metadata": {
    "papermill": {
     "duration": 0.003447,
     "end_time": "2025-10-22T22:32:01.844475",
     "exception": false,
     "start_time": "2025-10-22T22:32:01.841028",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h1>📌 Distribuição de Frequência em Python</h1>\n",
    "\n",
    "<p style=\"font-size:16px;\">A distribuição de frequência é uma das ferramentas mais fundamentais da estatística descritiva. Ela organiza e resume os dados, mostrando quantas vezes cada valor (ou intervalo de valores) aparece em um conjunto de observações.</p>\n",
    "\n",
    "<p style=\"font-size:16px;\">Em Python, podemos calcular e visualizar a distribuição de frequência de forma simples, utilizando bibliotecas como pandas, numpy e matplotlib. Neste artigo, você aprenderá passo a passo como construir uma tabela de frequência completa com:</p>\n",
    "<ul>\n",
    "    <li>📌 Classes (intervalos)</li>\n",
    "    <li>📌 Pontos médios</li>\n",
    "    <li>📌 Frequência absoluta</li>\n",
    "    <li>📌 Frequência acumulada</li>\n",
    "    <li>📌 Frequência relativa</li>\n",
    "    <li>📌 Frequência relativa acumulada</li>\n",
    "</ul>\n",
    "\n",
    "<h2>O que é uma Distribuição de Frequência?</h2>\n",
    "\n",
    "<p style=\"font-size:16px;\">Imagine que você tenha os dados de idades de 20 pessoas de um grupo. Esses valores podem ser muito variados, e olhar diretamente para a lista de números não ajuda muito. A distribuição de frequência agrupa esses dados em classes (intervalos), facilitando a visualização de como os valores se distribuem.</p>\n",
    "\n",
    "📌Autor: Carlos da Costa<br>\n",
    "📌Recife, PE - Brasil<br>\n",
    "📌Telefone: +55 81 99712 9140<br>\n",
    "📌Telegram: @jcarlossc<br>\n",
    "📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>\n",
    "📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>\n",
    "📌Email: jcarlossc1977@gmail.com<br>\n",
    "📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>\n",
    "📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>\n",
    "📌GitHub: https://github.com/jcarlossc<br>\n",
    "📌Kaggle: https://www.kaggle.com/jcarlossc/<br>\n",
    "📌Twitter/X: https://x.com/jcarlossc1977<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cddc6cd2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:01.853126Z",
     "iopub.status.busy": "2025-10-22T22:32:01.851883Z",
     "iopub.status.idle": "2025-10-22T22:32:03.845298Z",
     "shell.execute_reply": "2025-10-22T22:32:03.844072Z"
    },
    "papermill": {
     "duration": 1.998743,
     "end_time": "2025-10-22T22:32:03.847257",
     "exception": false,
     "start_time": "2025-10-22T22:32:01.848514",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Importa bibliotecas numpy(Matemática), pandas(Análise de Dados) e matplotlib(Gráficos).\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c5b62198",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:03.853205Z",
     "iopub.status.busy": "2025-10-22T22:32:03.852741Z",
     "iopub.status.idle": "2025-10-22T22:32:03.857839Z",
     "shell.execute_reply": "2025-10-22T22:32:03.856874Z"
    },
    "papermill": {
     "duration": 0.010364,
     "end_time": "2025-10-22T22:32:03.860002",
     "exception": false,
     "start_time": "2025-10-22T22:32:03.849638",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Exemplo de conjunto de dados: idades de 20 pessoas.\n",
    "idades = np.array([18, 22, 20, 24, 27, 19, 30, 34, 35, 28, 25, 23, 22, 21, 29, 31, 33, 37, 36, 35])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3712afe6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:03.867574Z",
     "iopub.status.busy": "2025-10-22T22:32:03.867265Z",
     "iopub.status.idle": "2025-10-22T22:32:03.872244Z",
     "shell.execute_reply": "2025-10-22T22:32:03.871024Z"
    },
    "papermill": {
     "duration": 0.010562,
     "end_time": "2025-10-22T22:32:03.874133",
     "exception": false,
     "start_time": "2025-10-22T22:32:03.863571",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Quantidade de elementos do array.\n",
    "n = len(idades)\n",
    "# Quantidade de classes(Intervaloe).\n",
    "k = int(np.ceil(np.sqrt(n)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c58b5d89",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:03.880240Z",
     "iopub.status.busy": "2025-10-22T22:32:03.879888Z",
     "iopub.status.idle": "2025-10-22T22:32:03.886203Z",
     "shell.execute_reply": "2025-10-22T22:32:03.884836Z"
    },
    "papermill": {
     "duration": 0.011242,
     "end_time": "2025-10-22T22:32:03.887799",
     "exception": false,
     "start_time": "2025-10-22T22:32:03.876557",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Encontrando o valor mínimo e máximo.\n",
    "minima_idade = min(idades)\n",
    "maxima_idade = max(idades)\n",
    "\n",
    "# Amplitude total.\n",
    "amplitude_total = maxima_idade - minima_idade\n",
    "\n",
    "# Amplitude de classe (intervalo).\n",
    "amplitude_classe = round(amplitude_total / k)\n",
    "\n",
    "# Criando os limites de classes.\n",
    "faixas = list(range(minima_idade, maxima_idade + amplitude_classe, amplitude_classe))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "37094f94",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:03.893537Z",
     "iopub.status.busy": "2025-10-22T22:32:03.893228Z",
     "iopub.status.idle": "2025-10-22T22:32:03.950311Z",
     "shell.execute_reply": "2025-10-22T22:32:03.949221Z"
    },
    "papermill": {
     "duration": 0.062052,
     "end_time": "2025-10-22T22:32:03.952088",
     "exception": false,
     "start_time": "2025-10-22T22:32:03.890036",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Classes</th>\n",
       "      <th>Ponto Médio</th>\n",
       "      <th>Frequência Absoluta</th>\n",
       "      <th>Frequência Acumulada</th>\n",
       "      <th>Frequência Relativa</th>\n",
       "      <th>Freq. Relativa Acumulada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>18---22</td>\n",
       "      <td>20.0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>0.20</td>\n",
       "      <td>0.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>22---26</td>\n",
       "      <td>24.0</td>\n",
       "      <td>5</td>\n",
       "      <td>9</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26---30</td>\n",
       "      <td>28.0</td>\n",
       "      <td>3</td>\n",
       "      <td>12</td>\n",
       "      <td>0.15</td>\n",
       "      <td>0.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30---34</td>\n",
       "      <td>32.0</td>\n",
       "      <td>3</td>\n",
       "      <td>15</td>\n",
       "      <td>0.15</td>\n",
       "      <td>0.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>34---38</td>\n",
       "      <td>36.0</td>\n",
       "      <td>5</td>\n",
       "      <td>20</td>\n",
       "      <td>0.25</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Classes  Ponto Médio  Frequência Absoluta  Frequência Acumulada  \\\n",
       "0  18---22         20.0                    4                     4   \n",
       "1  22---26         24.0                    5                     9   \n",
       "2  26---30         28.0                    3                    12   \n",
       "3  30---34         32.0                    3                    15   \n",
       "4  34---38         36.0                    5                    20   \n",
       "\n",
       "   Frequência Relativa  Freq. Relativa Acumulada  \n",
       "0                 0.20                      0.20  \n",
       "1                 0.25                      0.45  \n",
       "2                 0.15                      0.60  \n",
       "3                 0.15                      0.75  \n",
       "4                 0.25                      1.00  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Criando as classes e suas frequências.\n",
    "frequencia_absoluta = pd.cut(idades, bins=faixas, right=False).value_counts().sort_index()\n",
    "\n",
    "# Criando um DataFrame para organizar os resultados.\n",
    "tabela = pd.DataFrame({\n",
    "    \"Classes\": [f\"{intervalo.left}---{intervalo.right}\" for intervalo in frequencia_absoluta.index],\n",
    "    \"Ponto Médio\": [(intervalo.left + intervalo.right) / 2 for intervalo in frequencia_absoluta.index],\n",
    "    \"Frequência Absoluta\": frequencia_absoluta.values\n",
    "})\n",
    "\n",
    "# Frequência absoluta acumulada.\n",
    "tabela[\"Frequência Acumulada\"] = tabela[\"Frequência Absoluta\"].cumsum()\n",
    "\n",
    "# Frequência relativa.\n",
    "tabela[\"Frequência Relativa\"] = (tabela[\"Frequência Absoluta\"] / len(idades)).round(3)\n",
    "\n",
    "# Frequência relativa acumulada.\n",
    "tabela[\"Freq. Relativa Acumulada\"] = tabela[\"Frequência Relativa\"].cumsum().round(3)\n",
    "\n",
    "tabela\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "042a11da",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-22T22:32:03.958586Z",
     "iopub.status.busy": "2025-10-22T22:32:03.958285Z",
     "iopub.status.idle": "2025-10-22T22:32:04.236941Z",
     "shell.execute_reply": "2025-10-22T22:32:04.235929Z"
    },
    "papermill": {
     "duration": 0.283939,
     "end_time": "2025-10-22T22:32:04.238514",
     "exception": false,
     "start_time": "2025-10-22T22:32:03.954575",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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8fHx2LhxIyIiIhAWFqa6mjRaLcL79EGnTp2q/WuPNVXumoxGI2bOmoV6gYFynMeIe1OTRqtF927d4O/vb9PX3smTJ1EekijZXtlZ27Zt0atXL8TExFh83tIZlcDAQKSmpsLd3R1A9fyXRWWtKT4+Hu3bt8fQ6E/hV78hAEAAEJCggfKlWVr81hxLi5t/vll6XAIgLMYlCEjliJtyLC1uz5puXDyH/0RPxv79+9G6detq/9pjTZW7pvj4eDzyyCMYMvuTOx47eIywvqaU28eNffv2oWXLljZ97aWnp8Pb2xuZmZny+7cldr+YtricnBycP38ezz33XKljnJyc4OTkZBZ3cHAwu2PItDJKMu1Y5Y2XdidSReKSJFmMl5ZjReOVuSa9Xg+f+o1Qp0kLi8sm2zBCQmFhoXwKmK891lRWvDLUVFRUxGPHPSZuHzc0Go38WrnXrz2z+VYgX5ubNm0afvnlF1y8eBH79+/H4MGDodVqFaegiIiIqPqy6xmVy5cvY8SIEUhNTYWfnx8effRRHDx4EH5+fvZMi4iIiFTCro3K6tWr7bl4IiIiUjm7f48KERERUWnYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKqlqkZl3rx5kCQJU6ZMsXcqREREpAKqaVT++OMPLF26FA8//LC9UyEiIiKVUEWjkpOTg2eeeQZfffUVvLy87J0OERERqYSDvRMAgPHjxyMiIgK9evXCnDlzyhxbUFCAgoIC+XFWVhYAQK/XQ6/XAwA0Gg00Gg2MRiOMRqM81hQ3GAwQQtwxfuXKFaSmpirmAQCSJAGAYmxZcY1GAyGEIi5JEiRJsltcLTWdPn0aDg4O0EBAMhpuLUuSAEkDSRiBYuOFpAEkqfT47ekVceDW+PLENVpACGVckm6NLzVuhKTI5VbupcXtWZMGAjqdTt4GJfcPSZKg1WpL3W/udn/SarWQJEneT4vHAcBgMJQr7uDgACGEIl5a7qyp6tYEAI6OjiWOHTxG2Lom03HDaDTCYDDY/LVXHnZvVFavXo0///wTf/zxR7nGx8TEIDo62iweFxcHV1dXAICfnx9CQkKQmJiIGzduyGMCAgIQEBCAhIQEZGZmyvHg4GDUqlULx48fR15eHgAgLy8P4ydMwKmTJxEVFQWdTiePX7p0KbKyshAVFaXIYf78+XB3d8eYMWPkWGFhIebPn4/g4GCMGDFCjqekpGDp0qUICwtDRESEHL9w4QJWrVqFLl26oHPnznI8Pj4eGzduREREBMLCwuT4r7/+ir1792LEiBEIDg6W4xs3bkR8fDzGjBkDX19fOb5q1SpcuHBBdTU95JQP55QzAIAsVz9kufrBJ/MSnAtz5fHpbnWQ6+KF2umJcND/06ymeNZDvq4m6qadhVRsJ7nmHQKDxgEP3J6vyRXfUGiNevinnZdjQqPBFd/GcC7KhW9GkhzXOzjhmncIXPMz4JWdLMfzda5I8QyC+81UuOf+8xrLdfFEultdeOVcg2tehhxXQ00+TvmIiopCenq6vL0uXLggj/fw8ECTJk1w9epVXL58WY7bYn8CgMaNG8PT0xNxcXGKA9TDDz8MnU6H2NhYRU1t2rRBYWEhjh49Kse0Wi3atm2LzMxMnD59Wo67uLigRYsWrKka1QQAQ4YMURw7eIywfU0P3T5upKamIiEhwaavvZMnT6I8JFHyn8r30aVLl9CmTRts375dvjalW7duCAsLw0cffWRxGktnVAIDA5Gamgp3d3cAtvmXRXx8PNq3b48h73wO/wYNFTmY5ljyc7PS4xIAYTEuQUAqR1wAEGXENVBuxtLit3IsLX7/azq9bxd2fzkf477ZjLqhD92Kq/RfFpX9X0tXzxzDklER2L9/P1q3bs1/qbOmSl1TfHw8HnnkEbyyYlOxYwePEbauKfn0ESwZFYF9+/ahZcuWNn3tpaenw9vbG5mZmfL7tyV2PaNy+PBhXL9+Ha1atZJjBoMBe/fuxWeffYaCggJ5JzBxcnKCk5OT2bwcHBzg4KAsx7QySio5T0tx00qv1aAR6jRpUaG6qPz+TjwHvV4PI6RbO0wxt3ZE82lKjWssb1chVSAuSRWMayAs5FJa3J41GSGhsLBQ/jivtP2jovHy7E/FldxPrYlLkmQxzpqqV01FRUUVO3bwGFHhmkzHDY1GI79W7vVrryS7Nio9e/bEsWPHFLFRo0ahcePG+L//+79yF0FERERVk10bFTc3NzRv3lwRc3V1hY+Pj1mciIiIqh9V3J5MREREZInd7/opac+ePfZOgYiIiFSCZ1SIiIhItdioEBERkWqxUSEiIiLVYqNCREREqsVGhYiIiFSLjQoRERGpFhsVIiIiUi02KkRERKRabFSIiIhItdioEBERkWqxUSEiIiLVYqNCREREqsVGhYiIiFSLjQoRERGpFhsVIiIiUi02KkRERKRabFSIiIhItdioEBERkWqxUSEiIiLVYqNCREREqsVGhYiIiFSLjQoRERGploO1E65btw5r1qxBUlISCgsLFc/9+eefd50YERERkVVnVD755BOMGjUKtWvXRlxcHNq1awcfHx9cuHABjz32mK1zJCIiomrKqkbliy++wJdffolPP/0UOp0Or7/+OrZv345JkyYhMzPT1jkSERFRNWVVo5KUlISOHTsCAFxcXJCdnQ0AeO6557Bq1SrbZUdERETVmlWNir+/P9LS0gAA9erVw8GDBwEAiYmJEELYLjsiIiKq1qxqVHr06IGff/4ZADBq1Ci8+uqr6N27N4YPH47BgwfbNEEiIiKqvqy66+fLL7+E0WgEAIwfPx4+Pj7Yv38/Hn/8cYwZM8amCRIREVH1ZVWjcvnyZQQGBsqPn3rqKTz11FMQQuDSpUuoV6+ezRIkIiKi6suqj34aNGiAGzdumMXT0tLQoEGDu06KiIiICLCyURFCQJIks3hOTg6cnZ3vOikiIiIioIIf/bz22msAAEmS8Pbbb6NGjRrycwaDAYcOHUJYWJhNEyQiIqLqq0KNSlxcHIBbZ1SOHTsGnU4nP6fT6dCiRQtMmzbNthkSERFRtVWhRmX37t0Abt2S/PHHH8Pd3f2eJEVEREQEWHnXz/Lly22dBxEREZEZqxqVHj16lPn8rl27rEqGiIiIqDirGpUWLVooHhcVFSE+Ph7Hjx9HZGSkTRIjIiIisqpRWbRokcX47NmzkZOTc1cJEREREZlY9T0qpXn22Wfx9ddf23KWREREVI3ZtFE5cOAAv/CNiIiIbMaqj36eeOIJxWMhBJKTkxEbG4u3337bJokRERERWdWoeHh4KB5rNBqEhobinXfeQZ8+fWySGBERERG/R4WIiIhUy6bXqBARERHZUrnPqHh5eVn8xWRL0tLSrE6IiIiIyKTcjcpHH310D9MgIiIiMlfuRoXfOEtERET3m1UX0wKAwWDAjz/+iFOnTgEAmjVrhscffxxardZmyREREVH1ZlWjcu7cOfTr1w9XrlxBaGgoACAmJgaBgYHYuHEjQkJCbJokERERVU9W3fUzadIkhISE4NKlS/jzzz/x559/IikpCQ0aNMCkSZNsnSMRERFVU1adUfnll19w8OBBeHt7yzEfHx/MmzcPnTp1sllyREREVL1ZdUbFyckJ2dnZZvGcnBzodLq7ToqIiIgIsLJR6d+/P15++WUcOnQIQggIIXDw4EGMHTsWjz/+uK1zJCIiomrKqkblk08+QUhICDp06ABnZ2c4OzujU6dOaNiwIT7++GNb50hERETVlFXXqHh6euKnn37CuXPn5NuTmzRpgoYNG9o0OSIiIqrerP4eFQBo2LAhGjZsCIPBgGPHjiE9PR1eXl62yo2IiIiqOas++pkyZQqWLVsG4NYXv3Xt2hWtWrVCYGAg9uzZY8v8iIiIqBqzqlFZt24dWrRoAQD473//iwsXLuD06dN49dVX8eabb9o0QSIiIqq+rGpUUlJS4O/vDwDYtGkThg0bhgcffBAvvPACjh07Vu75LF68GA8//DDc3d3h7u6ODh06YPPmzdakRERERFWQVY1K7dq1cfLkSRgMBmzZsgW9e/cGANy8ebNCv/UTEBCAefPm4fDhw4iNjUWPHj0wcOBAnDhxwpq0iIiIqIqx6mLaUaNGYdiwYahTpw4kSUKvXr0AAIcOHULjxo3LPZ8BAwYoHr/33ntYvHgxDh48iGbNmlmTGhEREVUhVjUqs2fPRvPmzXHp0iUMHToUTk5OAACtVovp06dblYjBYMDatWuRm5uLDh06WDUPIiIiqlqsvj15yJAhZrHIyMgKz+fYsWPo0KED8vPzUbNmTWzYsAFNmzYtdXxBQQEKCgrkx1lZWQAAvV4PvV4PANBoNNBoNDAajTAajfJYU9xgMEAIUWbcaDRCo7n1yZhkNChyENLtuDCWL67RAkIo45J0a3ypcSOkYjkKSQLKiEvCCCjiGkCSSo+rpSYADg4O0EDIOVX6mlS6nTQQ0Ol08ncfmb5V+p+SJEiSdM/jxfdJU9yUT3niGo3GbrmXt6bCwkI4OTlVqZrUtp1Onz4NR0fHEscOHiNsXZPpuGE0GmEwGKDVakt9b7XmPbc8rG5Udu7ciUWLFim+8G3KlCnyx0DlFRoaivj4eGRmZmLdunWIjIzEL7/8UmqzEhMTg+joaLN4XFwcXF1dAQB+fn4ICQlBYmIibty4IY8JCAhAQEAAEhISkJmZKceDg4NRq1YtHD9+HHl5eQCAzMxM1K9fHwBQN+0spGIr/5p3CAwaBzyQckaRwxXfUGiNevinnZdjQqPBFd/GcC7KhW9GkhzXOzjhmncIXPMz4JWdLMfzda5I8QyC+81UuOf+k3uuiyfS3erCK+caXPMy5HiWqx+yXP3gk3kJzoW5cjzdrQ5yXbxQOz0RDvp/GrsUz3rI19VUTU0AEB4ejoec8uF8e9mVvSa1bicPKRNRUVH49ddf8eyzzyIsLAwRERHy+AsXLmDVqlXo0qULOnfuLMfj4+OxceNGREREICwsTI7/+uuv2Lt3L0aMGIHg4GA5vnHjRsTHx2PMmDHw9fWV46tWrcKFCxcQFRWl+E2wpUuXIisrC1FRUYqa5s+fD3d3d4wZM0aOFRYWYv78+QgODsaIESP+WV8pKVi6dKlqavryq6+QmZFRpWpS63YqfuzgMcL2NT3klI+oqCikpqYiISEBTZo0wdWrV3H58mV5vLXvuSdPnkR5SKJkG1wOX3zxBSZPnowhQ4bIH9McPHgQ69atw6JFizB+/PiKzlLWq1cvhISEYOnSpRaft3RGJTAwEKmpqXB3dwdgmzMq8fHxaN++Pcat3IaA0OaKHNiF266muM3rsX72RIz7ZjPqhj5UJWpS63Y6snUD/hM9GU/M+hi+9RtBgoAEJSMks7gAIMqIa6A8hJQWv5VZaXHzK/tLj0sAhMW4Gmo6e2APtnw+F0Pf/QL+DRpaGF/5aio7d/vUdHrfLuz5agFeWbGp2LGDxwhb15R8+giWjIrAvn370LJlS5ueUUlPT4e3tzcyMzPl929LrDqjMnfuXCxatAgTJkyQY5MmTUKnTp0wd+7cu2pUjEajohEpycnJSb4mpjgHBwc4OCjLMa2Mkkq7M6l43LTSgdsb0gIhVSAuSRWMayBK7sllxG+9aCsQV1FNer0eRkhmOVXmmtS4nQzi1r90fes3wgNNWlicnu7etcRzEEKgVoNGqMP1fM/8nXgORUVFFTt28BhR4ZqMkFBYWAiNRiO/R5b23no377llser25IyMDPTt29cs3qdPH8XpnTuZMWMG9u7di4sXL+LYsWOYMWMG9uzZg2eeecaatIiIiKiKsapRefzxx7Fhwwaz+E8//YT+/fuXez7Xr1/H888/j9DQUPTs2RN//PEHtm7dKn8vCxEREVVv5f7o55NPPpH/u2nTpnjvvfewZ88exTUq+/btw9SpU8u9cNPvBRERERFZUu5GZdGiRYrHXl5eOHnypOKqXU9PT3z99dd46623bJchERERVVvlblQSExPvZR5EREREZqy6RqU0p06dwrRp02w5SyIiIqrG7rpRyc3NxbJly9CxY0c0a9YMW7ZssUVeRERERNY3Kvv27cMLL7yA2rVr4+WXX0bHjh1x8uRJHD9+3Jb5ERERUTVWoUbl+vXr+OCDD9C4cWMMGTIEnp6e2LNnDzQaDV544YUK/XIyERER0Z1U6Jtpg4KCMGTIEHz88cfo3bu3xW+gIyIiIrKVCnUaQUFB+O2337B3714kJCTcq5yIiIiIAFSwUTl9+jS+++47JCcno23btmjdurX8/Sqmn/omIiIispUKf3bTqVMnfP3110hOTsbYsWOxdu1aGAwGjBs3Dl999ZXiJ56JiIiI7obVF5nUrFkTL730Evbv348TJ06gdevWeOutt1C3bl1b5kdERETVmE2uhm3SpAkWLFiAK1eu4IcffrDFLImIiIhs+820Dg4OeOKJJ2w5SyIiIqrGeH8xERERqRYbFSIiIlItNipERESkWmxUiIiISLUq9BX6xcXGxmLNmjVISkpCYWGh4rn169ffdWJEREREVp1RWb16NTp27IhTp05hw4YNKCoqwokTJ7Br1y54eHjYOkciIiKqpqxqVObOnYtFixbhv//9L3Q6HT7++GOcPn0aw4YNQ7169WydIxEREVVTVjUq58+fR0REBABAp9MhNzcXkiTh1VdfxZdffmnTBImIiKj6sqpR8fLyQnZ2NgDggQcewPHjxwEAGRkZuHnzpu2yIyIiomrNqotpu3Tpgu3bt+Ohhx7C0KFDMXnyZOzatQvbt29Hz549bZ0jERERVVNWNSqfffYZ8vPzAQBvvvkmHB0dsX//fjz55JN46623bJogERERVV9WNSre3t7yf2s0GkyfPt1mCRERERGZlLtRycrKgru7u/zfZTGNIyIiIrob5W5UvLy8kJycjFq1asHT0xOSJJmNEUJAkiQYDAabJklERETVU7kblV27dskf+ezevfueJURERERkUu5GpWvXrhb/m4iIiOhesep7VJYvX461a9eaxdeuXYtvvvnmrpMiIiIiAqxsVGJiYuDr62sWr1WrFubOnXvXSREREREBVjYqSUlJaNCggVk8KCgISUlJd50UEREREWBlo1KrVi0cPXrULH7kyBH4+PjcdVJEREREgJWNyogRIzBp0iTs3r0bBoMBBoMBu3btwuTJk/HUU0/ZOkciIiKqpqz6Ztp3330XFy9eRM+ePeHgcGsWRqMRzz//PK9RISIiIpuxqlHR6XT44Ycf8O677+LIkSNwcXHBQw89hKCgIFvnR0RERNWYVY2KyYMPPogHH3zQVrkQERERKVjVqBgMBqxYsQI7d+7E9evXYTQaFc/v2rXLJskRERFR9WZVozJ58mSsWLECERERaN68ucXf/SEiIiK6W1Y1KqtXr8aaNWvQr18/W+dDREREJLPq9mSdToeGDRvaOhciIiIiBasalalTp+Ljjz+GEMLW+RARERHJrPro57fffsPu3buxefNmNGvWDI6Ojorn169fb5PkiIiIqHqzqlHx9PTE4MGDbZ0LERERkYJVjcry5cttnQcRERGRGauuUQEAvV6PHTt2YOnSpcjOzgYAXL16FTk5OTZLjoiIiKq3Cp1RMRqN0Gg0+Ouvv9C3b18kJSWhoKAAvXv3hpubG95//30UFBRgyZIl9ypfIiIiqkbKfUbl2LFj6NKlC4BbX/jWpk0bpKenw8XFRR4zePBg7Ny50/ZZEhERUbVUrjMq69atwzvvvIPvvvsOAPDrr79i//790Ol0inH169fHlStXbJ8lERERVUvlOqNiNBphMBjkr8o3PS7p8uXLcHNzs22GREREVG2Vq1EZNmwYVq5ciZdffhkA0Lt3b3z00Ufy85Ik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NA54IOWMIocrvqHQGvXwTzsvx4RGgyu+jeFclAvfjCQ5rndwwjXvELjmZ8ArO1mO5+tckeIZBPebqXDP/Sf3XBdPpLvVhVfONbjmZcjxLFc/ZLn6wSfzEpwLc+V4ulsd5Lp4oXZ6Ihz0/zR2KZ71kK+rqZqaACA8PBwPOeXD+fayK3tNat1OboFeCI6Kgr+uADlAlajJRE3byS3QC9t9fKABqkxNgPq2EwAMGTJEceyo7DWpcTs95JSPqKgopKamIiEhAU2aNMHVq1dx+fJleby177knT55EeUiieJtjZ5IkYcOGDRg0aFCpYyydUQkMDERqairc3d0B2OaMSnx8PNq3b49xK7chILS5Igd24barKW7zeqyfPRHjvtmMuqEPVYma1LqdjmzdgP9ET8bY5RtRp0lYlajJPHf713Rk6wasfmscxn+3DQG3X9OVvaYyc7dTTXGb12ND9CS8smJTsWNH5a5Jjdsp+fQRLBkVgX379qFly5Y2PaOSnp4Ob29vZGZmyu/fllS6MypOTk5wcnIyizs4OMDBQVmOaWWUpNVqLc67eNy00oHbG9ICIVUgLkkVjGsgJAszLyV+60VbgbiKatLr9TBCMsupMtekxu1kEEBhYSGMpgVVgZrKH79/NRkEbh+UzV/T/8ynctWkHK+emoqKiip27KgENaltOxkhobCwEBqNRn6PLO299W7ec8tiPkciIiIilbD7GZWcnBycO3dOfpyYmIj4+Hh4e3ujXr16dsyMiIiI7M3ujUpsbCy6d+8uP37ttdcAAJGRkVixYoWdsiIiIiI1sHuj0q1bN6joel4iIiJSEV6jQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEhIiIi1WKjQkRERKrFRoWIiIhUi40KERERqRYbFSIiIlItNipERESkWmxUiIiISLXYqBAREZFqsVEh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yBrTpk3D9u3bsWDBAjRs2BAuLi4YMmQICgsLK5RrnTp1sGfPHrPn1HYbOJGasVEhqgYOHz4Mo9GIhQsXQqO5dWma6VqSskydOhUajQabN29Gv379EBERgR49egAA9u3bh44dO2LcuHHyeEtnClq2bImWLVtixowZ6NChA/79739bbFSaNGmClStXIj8/Xz6rcvDgQcWYVq1a4T//+Q/q168PBwfrDl9NmjRRNFOWlrNv3z6MHDlSPvOSk5ODixcvys83btwYer0ehw8fRtu2bQEAZ86cUdwC3apVK1y7dg0ODg6oX7++VbkSES+mJaoWGjZsiKKiInz66ae4cOECVq5ciSVLlpQ5zcaNG/H111/j+++/R+/evREVFYXIyEikp6cDABo1aoTY2Fhs3boVCQkJePvtt/HHH3/I0ycmJmLGjBk4cOAA/vrrL2zbtg1nz55FkyZNLC7v6aefhiRJeOmll3Dy5Els2rQJCxYsUIwZP3480tLSMGLECPzxxx84f/48tm7dilGjRsFgMJRrXZjO8CxYsABnz57FZ599pvjYx1Tb+vXrER8fjyNHjuDpp5+G0WiUnw8NDUXfvn0xZswYHDp0CIcPH8aLL76ouL27V69e6NChAwYNGoRt27bh4sWL2L9/P958803ExsaWK1ciAi+mJapKIiMjxcCBAy0+9+GHH4o6deoIFxcXER4eLr799lvFRabFL6a9fv26qF27tpg7d648fWFhoWjdurUYNmyYEEKI/Px8MXLkSOHh4SE8PT3FK6+8IqZPny5atGghhBDi2rVrYtCgQaJOnTpCp9OJoKAgMXPmTGEwGErN/8CBA6JFixZCp9OJsLAw8Z///EdxMa0QQiQkJIjBgwcLT09P4eLiIho3biymTJkijEajxXmWvJhWCCGWLVsmAgIChIuLixgwYIBYsGCB4mLaxMRE0b17d+Hi4iICAwPFZ599Jrp27SomT54sj0lOThYRERHCyclJ1KtXT3z77bciKChIvphWCCGysrLExIkTRd26dYWjo6MIDAwUzzzzjEhKSip1HRCRkiTE7S9JICIiIlIZfvRDREREqsVGhYiIiFSLjQoRERGpFhsVIiIiUi02KkRERKRabFSIiIhItdioEBERkWqxUSEiIiLVYqNCREREqsVGhYiIiFSLjQoRERGpFhsVIiIiUq3/B45tdUYbunJ2AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Histograma dos resultados.\n",
    "plt.hist(idades, bins=faixas, edgecolor='black', color='skyblue')\n",
    "plt.title(\"Histograma de Idades\")\n",
    "plt.xlabel(\"Faixas de Idade\")\n",
    "plt.ylabel(\"Frequência Absoluta\")\n",
    "plt.grid(axis='y', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 31153,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 7.643305,
   "end_time": "2025-10-22T22:32:04.761274",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-10-22T22:31:57.117969",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
