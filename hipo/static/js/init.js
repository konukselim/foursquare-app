$('#submitReq').click(function() {
  var look_for = $('#look_for').val();
  var location = $('#location').val();
});

$(document).ready(function() {
  $('#example').DataTable( {
    destroy: true,
    dom: 'B<"pull-left"f>rtip',
    order: [[2, "desc"]],
    language: {
      search: '<div class="pull-left">Filter Venues</div>'
    }
  } );
  
  var hisData = window.historyData;
  var dataLength = hisData.length;
  var numOfPages = Math.ceil(dataLength / 10);

  var startPage = window.page_number ? window.page_number : 1;
  if (dataLength) {
    $('#historyListId').addClass("collection with-header");

    $('#pagination-id').twbsPagination({
      totalPages: numOfPages,
      startPage: startPage,
      last: '',
      first: '',
      activeClass: 'active page-class',
      prev: '',
      next: '',
      pageClass: 'waves-effect',
      onPageClick: function(event, page) {
        createHistoryList(page);
      }
    });
  }

  if(window.page_number) {
    for(i=0; i < $('.waves-effect .page-link').length; ++i) {
      if($('.waves-effect .page-link')[i].text == window.page_number) {
        $('.waves-effect .page-link')[i].className = ('active page-class');
      }
    }
  }

} );

function createHistoryList (pageNumber) {
  $('#historyListId').empty();
  var token = $('input[name="csrfmiddlewaretoken"]').val();
  var a = '<li class="collection-header"><h4>Previous Searches</h4></li>';
  
  var i = (pageNumber - 1) * 10;
  var j = pageNumber * 10  <= window.historyData.length ?   (i + 10) : (i + (window.historyData.length % 10));

  for(; i < j; ++i) {
    
    a = a.concat('<li class="collection-item" style="line-height:40px;padding-top:0px;padding-bottom:0px">') 
    a = a.concat('<div class="row" style="margin-bottom: 0px;"><form method="POST" action=""><input type="hidden" name="csrfmiddlewaretoken" value="'+ token +'"><div class="col s10">');
    a = a.concat(window.historyData[i][1] + " in " 
    + window.historyData[i][2] + '</div><input name="history_id" type="hidden" value="' 
    + window.historyData[i][0] + '"/><div class="col s2"><button type="submit" name="get_history_btn" class="btn-flat"><i class="material-icons">send</i></button></div></form></div></li>');
  }
  
  
  $('#historyListId').append(a);
}