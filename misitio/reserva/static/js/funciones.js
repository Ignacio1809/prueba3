function validarCampos(){
    var nombre = document.getElementById("nombre").value;

if (nombre.trim() == ""){
    //alert("Debe ingresar el nombre");
    //document.getElementById("txt-nombre").style.backgroundColor = "#FFDAB9";
    document.getElementById("error-nombre").style.visibility = "visible";
}
else
{
    //alert("Gracias por ingresar el nombre");
    document.getElementById("error-nombre").style.visibility = "hidden";
}
}