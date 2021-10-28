document.addEventListener("submit", function (event) {
    event.preventDefault();
    const form = event.target;
    const p = document.querySelector("#form-res");
    let form_data = new FormData(form);
    let review_data = {};
    form_data.forEach((value, key) => review_data[key] = value);
    let review_json = JSON.stringify(review_data);
    fetch(form.action, {
      method: form.method,
      body: review_json,
    })
      .then(function (response) {
        if (response.ok){form.reset();
          response.text()
          .then(function(data) {p.innerText = data;});
        }
      })
      .catch(function (error) {console.error(error);});
});