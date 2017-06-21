function canonize(avs_no) {
	return avs_no.replace(/\./g, "")
}

function is_valid_avs_number (avs_no) {
  avs_no = canonize(avs_no);
	if (avs_no.length != 13) return false;
  
  var total = 0;
  
  for(var i = 0 ; i < 12 ; i+=2) {
      total += parseInt(avs_no[i]);
  }
  
  for (var i = 1 ; i < 12 ; i+=2) {
  		total += parseInt(avs_no[i]) * 3;
  }
  
  var expected_key = 0;
  var actual_key = parseInt(avs_no[12]);
  if (total % 10 != 0) {
      var round_ten_up = Math.floor(total/10) * 10 + 10;
      expected_key = round_ten_up - total;
  }
  
  return actual_key == expected_key;
}
