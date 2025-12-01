const form = document.getElementById("docking-form");
const output = document.getElementById("output");
const exhInput = form.elements["exhaustiveness"];
const exhSpan = document.getElementById("exhaustiveness-value");

exhSpan.textContent = exhInput.value;
exhInput.addEventListener("input", () => {
  exhSpan.textContent = exhInput.value;
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const data = {
    receptor_path: form.elements["receptor_path"].value,
    ligand_path: form.elements["ligand_path"].value,
    center_x: parseFloat(form.elements["center_x"].value),
    center_y: parseFloat(form.elements["center_y"].value),
    center_z: parseFloat(form.elements["center_z"].value),
    size_x: parseFloat(form.elements["size_x"].value),
    size_y: parseFloat(form.elements["size_y"].value),
    size_z: parseFloat(form.elements["size_z"].value),
    runs: parseInt(form.elements["runs"].value, 10),
    exhaustiveness: parseInt(exhInput.value, 10),
  };

  output.textContent = "Running docking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/dock", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const json = await res.json();
    output.textContent = JSON.stringify(json, null, 2);
  } catch (err) {
    output.textContent = "Error: " + err;
  }
});