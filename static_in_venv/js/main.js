$(document).ready(function () {
  console.log("object");
  $("#filter").change(function () {
    console.log($('input[name="found"]:checked').val());
    console.log($('input[name="timeRange"]:checked').val());
    // console.log($('input[type="checkbox"]').val());
    var sThisVal = "",
      data;
    $('input[type="checkbox"]').each(function () {
      data = this.checked ? $(this).val() : "";
      if (data != "") {
        sThisVal = sThisVal.concat(data);
        sThisVal = sThisVal.concat(",");
      }
    });

    console.log(sThisVal);
    $.get(
      "/insights/table/",
      {
        found: $('input[name="found"]:checked').val(),
        timeRange: $('input[name="timeRange"]:checked').val(),

        user: sThisVal,
      },
      function (data) {
        $("tbody").empty();
        $.each(data, function (key, value) {
          console.log(data);
          // var priceKey = key;
          var keyword = key;
          var found = value;
          $("tbody").append(
            "<tr><td colspan='2'>" +
              keyword +
              "</td><td>" +
              found +
              "</td></tr>"
          );
        });
      }
    );
  });

  // $("#all").click(function () {
  //   $("users").prop("checked", this.checked);
  // });
});
