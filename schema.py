import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

'''
■エンドポイント定義

・リクエスト例
{
  allDepartment {
    edges {
      node {
        id
      }
    }
  }
}
{
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}
'''
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    all_department= SQLAlchemyConnectionField(Department)

schema = graphene.Schema(query=Query)