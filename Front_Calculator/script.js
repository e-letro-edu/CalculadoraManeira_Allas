// script.js

function calcular() {
  const a = parseFloat(document.getElementById("numero1").value);
  const b = parseFloat(document.getElementById("numero2").value);
  const operacao = document.getElementById("operacao").value;

  // Se for raiz quadrada, só enviamos 'a'
  const dados = operacao === "V"
    ? { a, operacao }
    : { a, b, operacao };

  fetch("http://localhost:5000/calcular", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dados)
  })
  .then(res => res.json())
  .then(data => {
    const resEl = document.getElementById("resultado");
    if (data.resultado !== undefined) {
      resEl.classList.replace("alert-danger", "alert-dark");
      resEl.innerText = "Resultado: " + data.resultado;
    } else {
      resEl.classList.replace("alert-dark", "alert-danger");
      resEl.innerText = "Erro: " + data.erro;
    }
  })
  .catch(() => {
    const resEl = document.getElementById("resultado");
    resEl.classList.replace("alert-dark", "alert-danger");
    resEl.innerText = "Erro ao conectar com a API.";
  });
}
