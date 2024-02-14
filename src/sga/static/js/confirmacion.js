const btnEliminar = document.querySelectorAll('.btnEliminar');

btnEliminar.forEach(btn => {
    btn.addEventListener('click', event => {
        let confirmacion = confirm('¿Está seguro de retirar esta clase?');
        if (! confirmacion) {
            event.preventDefault()
        }
    })
});
