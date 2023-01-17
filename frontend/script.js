$(document).ready(function(){
	$('h2').mousedown(function(){
		let id = $(this).data('id');
		$('.expand-container[data-id="' + id + '"]').fadeIn('slow');
	});
	
	$('#classify-form').on('submit', function(event) {
		event.preventDefault();
		
		$.ajax({
			url: '/classify/',
			type: 'POST',
			data: new FormData(this),
			dataType: 'json',
			success: function (data) {
				console.log(data)
				$("#notify").notify("Class: " + data.class + ', accuracy: ' + data.accuracy, 'success');
			},
			error: function (obj, error) {
				console.error(error);
			},
			cache: false,
			contentType: false,
			processData: false
		});
	});
});