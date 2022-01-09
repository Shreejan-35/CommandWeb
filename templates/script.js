let registerButton = document.getElementById("registered");

registerButton.addEventlistener("click", function(){
    alert("SUCCESSFULLY REGISTERED!!");
    document.location.href = "/login";
})

let IsUsername = document.getElementById("IsUser");
let IsPassword = document.getElementById("IsPassword");
let Username = document.getElementById("UserName");

if (IsUsername.innerText == "True" && IsPassword.innerText == "True")
{
    let presentName = document.getElementById("name");
    presentName.innerText = "Welcome, " + Username.innerText;
}
