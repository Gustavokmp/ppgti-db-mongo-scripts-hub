db.eventosJP.find(
{ 
    data: { $gte: ISODate("2023-08-01T00:00:00Z"), $lte: ISODate("2023-08-31T23:59:59Z") 

} 
});