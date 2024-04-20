db.locaisJP.aggregate([
    {
        $lookup: {
            from: "eventosJP",
            localField: "_id",
            foreignField: "local_id",
            as: "eventos"
        }
    },
    {
        $match: {
            eventos: { $exists: true, $not: { $size: 0 } }
        }
    }
]);
