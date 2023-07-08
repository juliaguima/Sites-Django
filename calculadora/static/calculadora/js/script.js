
      
function calcular(tipo, valor) {

  if (tipo === 'acao') {

    if (valor === 'c') {
      document.getElementById('resultado').value = '' //limpar o visor
    }

    if (valor === '+' || valor === '-' || valor === '*' || valor === '/' || valor === '.') {
      document.getElementById('resultado').value += valor //concatena o símbolo com os valores no visor
    }

    if (valor === '=') {
      var valor_campo = eval(document.getElementById('resultado').value)
      document.getElementById('resultado').value = valor_campo //interpreta o valor da variavel como uma expressao aritmetica
    }

  } else if (tipo === 'valor') {
    document.getElementById('resultado').value += valor //valor aparece no visor
  }

}

