alter table employees
	drop column isInfected, 
	drop column infectionChance, 
	drop column interactionsPerDay;


-- Add column of isInfected
alter table employees
	add column isInfected bool;
update employees
	set isInfected = False;


-- Add column of infectionChance
alter table employees
	add column infectionChance float;
update employees 
	set infectionChance = 0.1;

-- add column of interactionsPerDay
alter table employees
	add column interactionsPerDay int;
update employees 
	set interactionsPerday = floor(random()*30)+1;
