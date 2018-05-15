create table chart(
  tanggal date,
  id int,
  harga int,
  jumlah int
)

insert into chart values(date, idx, harga, jml)
select curdate(), 1, barang.harga, 1
from barang
where barang.id=1;

insert into chart values(curdate(), 1, (select harga from barang where id=1), 1);
