$(function() {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-event").modal("show");
      },
      success: function (data) {
        $("#modal-event .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".w3ls-header-right #test ul").html(data.html_user);
          $("#modal-event").modal("hide");
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


//loginform
var signForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".w3ls-header-right ul").html(data.html_user);
          $("#modal-event").modal("hide");
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


//loginform
var loginForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".w3ls-header-right #top_navbar ul").html(data.html_user);
          $("#modal-event").modal("hide");
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create Event
  // $(".js-create-event").click(loadForm);
  // $("#modal-event").on("submit", ".js-event-create-form", saveForm);
  
  //Signup Form
  $(".js-user-signup").click(loadForm);
  $("#modal-event").on("submit", ".js-user-create-form", saveForm);
  
  //Login Form
  $(".js-user-login").click(loadForm);
  $("#modal-event").on("submit", ".js-user-login-form",saveForm );

  $(".js-user-logout").click(loadForm);
  $("#modal-event").on("submit", ".js-user-logout-form",saveForm );
  
  

  // // Update Event
  // $("#event-table").on("click", ".js-update-event", loadForm);
  // $("#modal-event").on("submit", ".js-event-update-form", saveForm);

  // // Delete book
  // $("#event-table").on("click", ".js-delete-event", loadForm);
  // $("#modal-event").on("submit", ".js-event-delete-form", saveForm);

});
