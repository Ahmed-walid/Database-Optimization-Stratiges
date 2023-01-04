CREATE INDEX complaintDateIndex USING BTREE ON complaints(DATE);
CREATE INDEX offerPriceIndex USING BTREE ON offer(PRICE);
CREATE INDEX serviceCostIndex USING BTREE ON service(COST);
CREATE INDEX cardValueIndex USING BTREE ON card(VALUE);