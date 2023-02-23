create database Tutorat;
use tutorat;
create table student(
matricule int not null,
first_name varchar(10),
Last_name varchar(10),
primary key(matricule)
);
	
insert into student values('1196796', 'Younes','Alaoui');
insert into student values('6776576', 'Jack','Born');
insert into student values('3444545', 'Sophia','mergentey');
insert into student values('4353546', 'Ali','Sabouhi');
select * from student