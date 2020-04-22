function newDate(days) {
			return moment().add(days, 'd').toDate();
		}

function newDateString(days) {
			return moment().add(days, 'd').format();
		}

var config = {}
var input_data = {}
var startIndex = 0;

function isLeap(year){
  return ((year%4 ==0 && year%100 !=0) || (year%400 == 0));
}
function index(endYear,endMonth,endDay){
  daysOfMonth = {1:31,
                 2:28,
                 3:31,
                 4:30,
                 5:31,
                 6:30,
                 7:31,
                 8:31,
                 9:30,
                 10:31,
                 11:30,
                 12:31}
  startYear = 2020
  count = 0

  for(var year = startYear;year<endYear;year++){
        if(isLeap(year)){
            count+=366;
        }else{
            count+=365;
        }

  }

  for(var month=1;month<endMonth;month++){
        if(month == 2 && isLeap(endYear)){
            count+=29;
        }else{
            count+=daysOfMonth[month];
        }
  }

  count+=endDay;


  return count

}




function selectedYear(year){

   // var e = document.getElementById(dropdownId);
   // var strUser = e.options[e.selectedIndex].text;

    window.console.log("Button Clicked",year);
    window.console.log("Index",index(year,12,31));

    limitIndex = index(year,12,31) ;



    if (config.data.datasets.length > 0) {
        var arrayToPlot = input_data['dataset_pred']['data_plot'].slice(startIndex,limitIndex);
        window.console.log("arrayTPlot",arrayToPlot.length);

        arrayToPlot.forEach(pushingData);

        function pushingData(item){
        //window.console.log("Item",item)
        config.data.datasets[1].data.push(item);

        }

        var labelsToPlot = input_data['dataset_pred']['label_plot'].slice(startIndex,limitIndex);

        labelsToPlot.forEach(pushingLabels);

        function pushingLabels(item){
        config.data.labels.push(item);
         //window.console.log("Item",item);


        }




        window.myLine.update();
        window.console.log("config",config);


    var predictedTraffic = document.getElementById('predictedTraffic');

    predictedTraffic.innerHTML = "Predicted Traffic : "+input_data['dataset_pred']['data_plot'][limitIndex-1].y;


    }

    startIndex = limitIndex+1;









}




function myFuncLine(input_data1) {
    input_data = input_data1
    console.log(input_data)
    var ctx = document.getElementById('canvas').getContext('2d');

    var color = Chart.helpers.color;
 config = {
    type: 'line',
    data: {
      labels: input_data['dataset_train']['label_plot'],
      datasets: [{
					label: 'Traffic density',
					data: input_data['dataset_train']['data_plot'],
					lineTension: 0,
                    backgroundColor: 'transparent',
                    borderColor: '#007bff',
                    borderWidth: 1,
                    pointBackgroundColor: '#007bff',
                    backgroundColor: color(window.chartColors.purple).alpha(0.5).rgbString(),
                    fill: true

				}

      ,{
        label : 'Traffic density',
        data: [],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: color(window.chartColors.red).alpha(0.5).rgbString(),
        borderWidth: 1,
        pointBackgroundColor: '#FF7bff',
        backgroundColor: color(window.chartColors.orange).alpha(0.5).rgbString(),
		fill: true
      }

      ]
    },
    options: {
      scales: {
      xAxes: [{
        display: true,
        scaleLabel: {
            display: true,
            labelString: 'Day of the Year',
            fontColor: color(window.chartColors.red).alpha(0.9).rgbString()
        }
        }],
        yAxes: [{
        display: true,
        scaleLabel: {
            display: true,
            labelString: 'value',
            fontColor: '#0000FF'
        },
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false
      }
    }
  };





    window.myLine = new Chart(ctx, config);
   // window.console.log(config.data.datasets[0].data)
};

