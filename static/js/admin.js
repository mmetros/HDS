// if (jQuery):
//   alert("jQuery is activated")


$(function() {
  $('#process_input').on('click', function() {
    $.getJSON('/_background_process', {
      name: $('input[name="m_name"]').val(),
      link: $('input[name="m_link"]').val(),
      logo: $('input[name="m_logo"]').val(),
      prod_cat: $('input[name="prod_cat"]').val()

    }, function(data) {
      // var txt = $("<p></p>").text(data.result);
      // $("#result").append(txt);
      alert(data.result)
    });
    return false;
  });
});
