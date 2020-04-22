/* globals Chart:false, feather:false */


function myFunc(input_data) {
    console.log(input_data)
    //window.alert("Function Called")


  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart').getContext('2d');


  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: input_data['label'],
      datasets: [{
        data: input_data['value'],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 1,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

}


/*
(function () {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')

  var lbl = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ]
   var values = [
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034,
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034,
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034
        ]

  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: lbl,
      datasets: [{
        data: values,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 1,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
}())
*/