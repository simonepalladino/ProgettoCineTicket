function demo() {
  var c = "ABCDEFGHIJKLMNOPQRSTUVWXTZ0123456789abcdefghiklmnopqrstuvwxyz";
  var strlength = 8;
  var random = '';
  for (var i=0; i<strlength; i++) {
    var num = Math.floor(Math.random() * c.length);
    random += c.substring(num,num+1);
  }
  document.rdform.random.value = random;
}
