Meu Portfólio de Data Science

Analisador de Oportunidades Imobiliárias

Este projeto faz parte do meu portfólio de **Ciência de Dados** aplicada ao mercado imobiliário. O objetivo é automatizar a identificação de imóveis com preço abaixo da média de mercado (oportunidades), auxiliando na tomada de decisão estratégica.

Funcionalidades
Análise por Bairro:** Identifica variações de preço em diferentes regiões.
Cálculo de m²:** Normaliza os valores para comparação direta.
Lógica de Alerta:** Detecta automaticamente quando um imóvel está com preço de "Oportunidade" baseado em um limite pré-definido.

Tecnologias Utilizadas
Python 3**: Linguagem principal para o processamento dos dados.
Git/GitHub**: Controle de versão e hospedagem do código.
Fedora Linux**: Ambiente de desenvolvimento.

Como o Analisador funciona
O script processa os dados e aplica a seguinte lógica:
- Se o `preço_m2` for menor que o `LIMITE_OPORTUNIDADE`, o sistema gera um alerta visual: ` OPORTUNIDADE DETECTADA!`.
- Caso contrário, o status permanece como `Preço Normal`.

---
Desenvolvido por Getúliojr08         
