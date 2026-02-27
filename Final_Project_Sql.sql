SELECT * FROM census_analysis.census_data;
drop table census_data
create table census_data (
State varchar(10),
Area_Name varchar(50),	
Age	varchar(10),
Total_Population int,
Total_Males	int,
Total_Females	int,
Rural_Persons  	int,
Rural_Males	int,
Rural_Females	int,
Urban_Persons  	int,
Urban_Males	int,
Urban_Females	int,
Age_Category	varchar(10),
Gender_Ratio	decimal(10,2),
Urban_Percentage	decimal(10,2),
Rural_Percentage decimal(10,2))

select * from census_data
Count of Data
SELECT COUNT(*) FROM census_data;
/*Count of all Ages*/
SELECT COUNT(*) FROM census_data where age="All Ages"

/*Total Population by Area (All Ages)*/
SELECT Area_Name, Total_Population FROM census_data WHERE Age = 'All ages';

-- Gender Distribution
select Area_Name, Total_Males, Total_Females from census_data where Age = 'All ages';

-- Gender Ratio
select Area_Name, Gender_Ratio from census_data where age = "All Ages"

-- Rural vs Urban Population
select Area_Name, Rural_Persons ,Urban_Persons from census_data where age = "All Ages"

-- Age-wise Population Distribution
select age,sum(Total_Population) as Population from census_data  group by age order by age