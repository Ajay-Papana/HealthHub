<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function(){
        $('#aiForm').submit(function(e){
            e.preventDefault();
            var formData = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: 'your_endpoint.php', // Change this to your actual endpoint
                data: formData,
                success: function(response){
                    $('#aiResult').html(response);
                }
            });
        });
    });
</script>