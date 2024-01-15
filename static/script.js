document.getElementById('submitBtn').addEventListener('click', function() {
  var nameInput = document.getElementById('nameInput');
  var name = nameInput.value;

  if (name !== '') {
    var welcomeMessage = 'Welcome, ' + name + '!';
    alert(welcomeMessage);
    nameInput.value = '';
  } else {
    alert('Please enter your name.');
  }
});
