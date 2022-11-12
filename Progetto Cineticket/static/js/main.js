function SaveStudentDetails() {
    validateControls();
}
var gender;
var email_reg_exp = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-]{2,})+.)+([a-zA-Z0-9]{2,})+$/;
function validateControls() {
    //FirstName
    var fname = document.getElementById("fname")
    if (fname.value == "") {
        window.alert("please enter your first name");
        fname.focus();
        return false;
    }
    //LastName
    var lname = document.getElementById("lname")
    if (lname.value == "") {
        window.alert("please enter your last name");
        lname.focus();
        return false;
    }
    //Email
    var email = document.getElementById("email")
    if (!email_reg_exp.test(email) || (email.value == "")) {
        window.alert("please enter your valid email ");
        email.focus();
        return false;
    }
    //Password
    var password = document.getElementById("email")
    if ((password.value == "")) {
      window.alert("please enter your valid password ");
      password.focus();
      return false;
  }
    //Mobile
    var mobile = document.getElementById("mobile")
    if (mobile.value == "") {
        window.alert("please enter your 10 digits mobile no.");
        mobile.focus();
        return false;
    }
    //Gender
    gender = document.querySelector('input[name="gender"]:checked');
    if (gender === null) {
        window.alert("Gender required!");
        gender.focus();
        return false;
    }
    //Dob
    var dob = document.getElementById("dob")
    if (dob.value == "") {
        window.alert("please enter your Date of Birth");
        dob.focus();
        return false;
    }
    //Address
    var address = document.getElementById("address")
    if (address.value == "") {
        window.alert("please enter your address details");
        address.focus();
        return false;
    }
    //City
    var city = document.getElementById("city")
    if (city.value == "") {
        window.alert("please enter your city name");
        city.focus();
        return false;
    }
    // Pin
    var pin = document.getElementById("pin")
    if (pin.value == "") {
        window.alert("please enter your 6 digits Area PIN");
        pin.focus();
        return false;
    }
    // State
    var state = document.getElementById("state")
    if (state.value == "") {
        window.alert("please enter your state name");
        state.focus();
        return false;
    }

    getControlValues();

}
function getControlValues() {
    alert("First Name= " + fname.value + "\n" + "Last Name= " + lname.value + "\n"
        + "Email= " + email.value + "\n" + "Mobile= " + mobile.value + "\n"
        + "Gender= " + gender.value + "\n" + "DateOfBirth= " + dob.value + "\n"
        + "Address= " + address.value + "\n" + "City= " + city.value + "\n" + "Pin= "
        + pin.value + "\n" + "State= " + state.value + "\n")
}

function validate(){
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
    if(email=="raffaele.montella@uniparthenope.it" && password=="Montella72") {
        alert ("login succesfully");
    }
    else if (email=="simonepalladino@uniparthenope.it" && password=="palladin0&")
    {
      alert ("login succesfully");
    }
    else {
        alert ("login failed");
    }
}
