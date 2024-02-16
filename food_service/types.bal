import ballerina/graphql.subgraph;

@subgraph:Entity {
    key: "id"
}
public type Product record {
    readonly string id;
    string title;
    string description;
    int price;
    Category category;
};

public type Category record {
    string id;
    string title;
};