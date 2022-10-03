function obtenerdatos(id){
    document.getElementById('formulario').action='/editar_persona/'+id
    document.getElementById('boton_form').innerHTML='Actualizar'
    nombreactual=document.getElementById('tabla_nombre'+id).innerHTML
    apellidoactual=document.getElementById('tabla_apellido'+id).innerHTML
    edadactual=document.getElementById('tabla_edad'+id).innerHTML
    document.getElementById('nombre').value =nombreactual
    document.getElementById('apellido').value =apellidoactual
    document.getElementById('edad').value =edadactual
}

function obtenerusuario(id){
    document.getElementById('formulario').action='/editar_persona/'+id
    document.getElementById('boton_form').innerHTML='Actualizar'
    nombreactual=document.getElementById('tabla_nombre'+id).innerHTML
    apellidoactual=document.getElementById('tabla_apellido'+id).innerHTML
    edadactual=document.getElementById('tabla_edad'+id).innerHTML
    document.getElementById('nombre').value =nombreactual
    document.getElementById('apellido').value =apellidoactual
    document.getElementById('edad').value =edadactual
}