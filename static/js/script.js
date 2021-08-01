$('.remove-item').click(function () {
    let id = $(this).attr("product_id").toString()

    $.ajax({
        type: "GET",
        url: "/removed",
        data: {
            pid: id
        },
        success: (data) => {
            document.getElementById("total_price").innerText = data.total_price
        }
    })
})