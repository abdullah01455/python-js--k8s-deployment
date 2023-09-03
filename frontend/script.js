document.addEventListener('DOMContentLoaded', function() {
  // Get references to the buttons
  var button1 = document.getElementById('button-1');
  var button2 = document.getElementById('button-2');
  var button3 = document.getElementById('button-3');
  var button4 = document.getElementById('button-4');
  var button5 = document.getElementById('button-5');

  // Add event listeners to the buttons
  button1.addEventListener('click', function() {
    executeRequest('/vac');
  });

  button2.addEventListener('click', function() {
    executeRequest('/sic');
  });

  button3.addEventListener('click', function() {
    executeRequest('/qua');
  });

  button4.addEventListener('click', function() {
    executeRequest('/ind');
  });

  button5.addEventListener('click', function() {
    executeRequest('/hea');
  });

  // Function to execute the request to the backend API
  function executeRequest(endpoint) {
    fetch(endpoint)
      .then(response => response.json())
      .then(data => {
        // Handle the response from the backend if needed
        console.log(data);
      })
      .catch(error => {
        // Handle any errors that occur during the request
        console.error('Error:', error);
      });
  }
});