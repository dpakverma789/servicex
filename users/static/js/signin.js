
function visibility()
	{
  		var password = document.getElementById("password");
  		if (password.type === "password")
  		 {
    		password.type = "text";
  		 }
  		else

  		 {
    		password.type = "password";
  		 }

	}

function focusFunction(event){
    event.currentTarget.style.borderColor = '#f4ac08';
}